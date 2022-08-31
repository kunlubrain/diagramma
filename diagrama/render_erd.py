from jinja2 import (
    FileSystemLoader, 
    Environment
)
import fire


data = {
    "subgraphs": [
        {
            "name": "subgraph1",
            "label": "Schema",
            "bgcolor": "#222222",
            "nodebgcolor": "#ffffff",
            "nodes": [
                {
                    "name": "A",
                    "label": "A A",
                    "strokecolor": "#123456",
                    "bgcolor": "#654321",
                },
                {
                    "name": "B",
                    "label": "B B",
                    "strokecolor": "#00bb00",
                    "bgcolor": "#0000ff",
                }
            ],
            "edges": [
                {
                    "source": "A",
                    "target": "B"
                }
            ]
        }
    ]
}

def render(
    templatefile: str,
    dotfile: str):

    templateLoader = Environment(
        loader=FileSystemLoader(searchpath="templates/gv/")
        )

    tmpl = templateLoader.get_template(name=templatefile)
    rendered = tmpl.render(data)
    with open(dotfile, 'w') as fh:
        fh.write(rendered)
    print(f"Generated dot file: {dotfile}")

def test():
    ERD_TEMPLATE = "erd.gv"
    ERD_DOT_FILE = "erd/kg.dot"
    render(templatefile=ERD_TEMPLATE, dotfile=ERD_DOT_FILE)

if __name__=="__main__":
    fire.Fire(render)