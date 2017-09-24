#!/usr/bin/env python3
'''
Script for converting HTML documents into a YAML representation.
'''

import argparse

from bs4 import BeautifulSoup, element
import yaml


class Visitor:

    def walk(self, target):

        if type(target) == element.NavigableString:

            self.on_leaf(target)

        else:

            if target.parent:

                self.on_start_branch(target)

            if hasattr(target, 'children'):
                for child in target.children:
                    self.walk(child)

            if target.parent:
                self.on_end_branch(target)

    def on_start_branch(self, item):
        pass

    def on_end_branch(self, item):
        pass

    def on_leaf(self, item):
        pass


class TokenVisitor(Visitor):

    def __init__(self, token_cls):

        self.token_cls = token_cls

        self.active_token = self.token_cls(parent=None, name=None)

    def on_start_branch(self, item):

        new_token = self.token_cls(
            parent=self.active_token,
            name=item.name
        )

        if hasattr(item, 'attrs'):
            new_token.attribs = {k: v for k, v in item.attrs.items()}

        if hasattr(item, 'children'):
            self.active_token.children.append(new_token)

        self.active_token = new_token

    def on_end_branch(self, item):

        if self.active_token and self.active_token.parent:
            self.active_token = self.active_token.parent

    def on_leaf(self, item):

        text = item.string.strip()

        if text:
            self.active_token.text = text

    @property
    def dict(self):
        return self.active_token.dict


class Token:

    def __init__(self, parent, name):

        self.parent = parent
        self.name = name
        self.text = None
        self.attribs = {}
        self.children = []

    def close(self):
        pass

    @property
    def dict(self):

        if not self.name and not self.parent and not self.attribs:
            return [child.dict for child in self.children]

        retval = {
            '_name': self.name,
        }

        if self.attribs:
            retval['attribs'] = self.attribs

        if self.children:
            retval['subs'] = [child.dict for child in self.children]

        return retval


class FormattedToken(Token):

    @property
    def dict(self):

        if not self.name and not self.parent and not self.attribs:
            return [child.dict for child in self.children]

        retval = {
            self.name: {}
        }

        if self.text is not None:
            retval[self.name]['text'] = self.text

        if self.attribs:
            retval[self.name]['attribs'] = self.attribs

        if self.children:
            retval[self.name]['subs'] = [
                child.dict for child in self.children
            ]

        return retval


def main(filename, token_cls):

    html_doc = open(filename, 'r').read()

    soup = BeautifulSoup(html_doc, 'html.parser')

    visitor = TokenVisitor(token_cls=token_cls)

    visitor.walk(soup)

    yaml_data = yaml.dump(visitor.dict, default_flow_style=False)

    print(yaml_data)

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description=__doc__)

    parser.add_argument('filename', action='store', metavar='filename',
                        help='filename of the html file to process')

    parser.add_argument('--explicit',
                        default=False,
                        action='store_const',
                        const=True,
                        help='do not use element name shorthand')

    args = parser.parse_args()

    token_cls = Token if args.explicit else FormattedToken

    main(args.filename, token_cls)
