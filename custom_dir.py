import argparse
from docutils import nodes
from docutils.parsers.rst import directives, Directive

import hovercraft


class CSVTableDirective(Directive):
    """
    A custom directive to create a table from CSV-like formatted content.

    Example usage in a reST document:

    .. csvtable::
        :header: "Name", "Age", "City"

        John, 30, "New York"
        Anna, 28, "San Francisco"
        Mike, 32, "Chicago"
    """
    required_arguments = 0
    optional_arguments = 0
    final_argument_whitespace = True
    option_spec = {
        'header': directives.unchanged_required,
    }
    has_content = True

    def run(self):
        # Parse the header option
        header_row = [header.strip() for header in self.options['header'].split(',')]
        
        # Create a table node
        table = nodes.table()
        tgroup = nodes.tgroup(cols=len(header_row))
        table += tgroup
        
        # Add column specs
        for _ in header_row:
            tgroup += nodes.colspec(colwidth=1)
        
        # Create the header part of the table
        thead = nodes.thead()
        tgroup += thead
        header = nodes.row()
        thead += header
        for header_cell in header_row:
            entry = nodes.entry()
            header += entry
            entry += nodes.paragraph(text=header_cell)
        
        # Create the body part of the table
        tbody = nodes.tbody()
        tgroup += tbody
        for row in self.content:
            row_data = nodes.row()
            tbody += row_data
            for cell in row.split(','):
                entry = nodes.entry()
                row_data += entry
                entry += nodes.paragraph(text=cell.strip('"').strip())

        return [table]



directives.register_directive('csvtable', CSVTableDirective)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('action', choices=('run', 'build'), help='how to run hovercraft')
    args = parser.parse_args()
    if args.action == 'run':
        cmd = ['--skip-help', '-p', '5555', 'bigtable_talk.rst']
    else:
        cmd = ['--skip-help', '-p', '5555', 'bigtable_talk.rst', 'docs']
    hovercraft.main(cmd)

