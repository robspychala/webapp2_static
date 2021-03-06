# webapp2_static

Simple handler to Serve static files on non Google App Engine (GAE) webapp2 environments

```python
import webapp2_static

app = webapp2.WSGIApplication([
    (r'/', example.IndexHandler),
    (r'/static/(.+)', webapp2_static.StaticFileHandler)
], config = {'webapp2_static.static_file_path': './app/static'})
```

# Defaults

If the ```webapp2_static.static_file_path``` configuration option is omitted then the files are assumed to be located under the ```./static``` directory.

# Installation

Easiest way to install is from PyPI

```pip install webapp2_static```

and you're done.

# License

The simpledict component is released under the MIT License.

The MIT License (MIT) Copyright (c) 2012 Robert Spychala

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.