# Deoplete Markdown Links

Complete wiki links and tags in Markdown.

## Requirements

* [deoplete](https://github.com/Shougo/deoplete.nvim)
* [ripgrep](https://github.com/BurntSushi/ripgrep)

## Installation

```vim
Plug 'bouk/deoplete-markdown-links'
```

## Usage

Just type `[[` or `#` and files/tags in the same directory as the file will be auto-completed. That's it.

## Configuration

### Markdown Links

You can customize how you want files displayed for Markdown link completion by setting `g:deoplete#sources#markdown_links#name_pattern` to a pattern regex. It can optionally contain a `name` group.
If the regex doesn't match, the whole filename is used by default.
