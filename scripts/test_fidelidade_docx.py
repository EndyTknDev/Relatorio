import tempfile
import unittest
from pathlib import Path
from xml.etree import ElementTree as ET
from zipfile import ZipFile
from fidelidade_docx import W, comparar, substituir_em_trecho


class FidelidadeTest(unittest.TestCase):
    def setUp(self):
        self.root = ET.fromstring(f'<w:document xmlns:w="{W[1:-1]}"><w:body><w:p><w:r><w:rPr><w:b/></w:rPr><w:t>Município: </w:t></w:r><w:r><w:t>Acará</w:t></w:r></w:p></w:body></w:document>')

    def package(self, path, root):
        with ZipFile(path, 'w') as z:
            z.writestr('word/document.xml', ET.tostring(root))

    def test_rejects_collapse_but_accepts_value_edit(self):
        with tempfile.TemporaryDirectory() as folder:
            a, b = Path(folder)/'a.docx', Path(folder)/'b.docx'
            self.package(a, self.root)
            p = next(self.root.iter(W+'p'))
            substituir_em_trecho(p, 'Acará', 'Eirunepé')
            self.package(b, self.root)
            self.assertFalse(comparar(a, b)['erros'])
            nodes = list(p.iter(W+'t'))
            nodes[0].text = 'Município: Eirunepé'
            nodes[1].text = ''
            self.package(b, self.root)
            self.assertTrue(any('formatos' in e for e in comparar(a, b)['erros']))

    def test_refuses_cross_format_substitution(self):
        p = next(self.root.iter(W+'p'))
        with self.assertRaises(ValueError):
            substituir_em_trecho(p, 'Município: Acará', 'Município: Eirunepé')


if __name__ == '__main__':
    unittest.main()
