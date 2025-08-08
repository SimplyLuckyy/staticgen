from blocks import markdown_to_html_node
import os

def extract_title(markdown):
    if not markdown.strip().startswith("# "):
        raise Exception("No header")
    heading = markdown.splitlines()[0]
    heading = heading.replace("#", "").strip()
    return heading

def generate_page(from_path, template_path, destination_path):
    print(f"* Generating page from {from_path} to {destination_path} using {template_path}")

    markdownfile = open(from_path, "r").read()
    open(from_path, "r").close()
    templatefile = open(template_path, "r").read()
    open(template_path, "r").close()

    node = markdown_to_html_node(markdownfile)
    html = node.to_html()

    title = extract_title(markdownfile)

    templatefile = templatefile.replace("{{ Title }}", title)
    templatefile = templatefile.replace("{{ Content }}", html)
    

    end_path = os.path.dirname(destination_path)
    if end_path != "":
        os.makedirs(end_path, exist_ok=True)
    end_file = open(destination_path, "w")
    end_file.write(templatefile)
