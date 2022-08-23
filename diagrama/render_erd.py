from jinja2 import (
    FileSystemLoader, 
    Environment
)

templateLoader = Environment(
    loader=FileSystemLoader(searchpath="templates/gv/")
    )

ERD_TEMPLATE = "erd.gv"
ERD_DOT_FILE = "erd/kg.dot"

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
tmpl = templateLoader.get_template(name=ERD_TEMPLATE)
dotfile = tmpl.render(data)
with open(ERD_DOT_FILE, 'w') as fh:
    fh.write(dotfile)
print(f"Generated dot file: {ERD_DOT_FILE}")