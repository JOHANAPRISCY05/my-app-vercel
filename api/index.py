import json
from http.server import BaseHTTPRequestHandler
import urllib.parse

# List of student marks as dictionaries
student_marks = [{"name":"hPZTeg","marks":33},{"name":"ucIF7L","marks":60},{"name":"FHpnPdi","marks":38},{"name":"Y5E6KJQsF","marks":66},{"name":"B7Bfrp7","marks":13},{"name":"0e4ovvtj","marks":82},{"name":"4lTJW","marks":40},{"name":"2vL","marks":42},{"name":"NSVK","marks":57},{"name":"OPl4v2","marks":27},{"name":"dMPm89tU","marks":20},{"name":"s6ecnv","marks":80},{"name":"grBmXBny","marks":58},{"name":"h5e","marks":17},{"name":"V0g7Wp","marks":53},{"name":"ccU3cF1OgL","marks":4},{"name":"ipaXvBsci","marks":81},{"name":"vmzexfH","marks":2},{"name":"s","marks":75},{"name":"dP","marks":25},{"name":"QjX0C","marks":99},{"name":"PIXXfxNKOA","marks":79},{"name":"N9L1WSWhR","marks":60},{"name":"JD0qIarc","marks":12},{"name":"hYyx","marks":65},{"name":"3e","marks":37},{"name":"kF474Zj","marks":43},{"name":"bccF","marks":38},{"name":"UFIQfHW","marks":89},{"name":"fHYbA","marks":44},{"name":"hc5","marks":28},{"name":"wHT","marks":41},{"name":"K","marks":73},{"name":"BH2XN","marks":6},{"name":"dk","marks":24},{"name":"NToh1MJ2","marks":22},{"name":"AtYrrCz","marks":9},{"name":"xcMeAwC","marks":62},{"name":"2aib8m","marks":3},{"name":"vbdr","marks":97},{"name":"M","marks":26},{"name":"8","marks":61},{"name":"P4zH","marks":63},{"name":"2ql3p","marks":34},{"name":"Qmh","marks":85},{"name":"s","marks":66},{"name":"7O","marks":51},{"name":"uINS","marks":56},{"name":"wN5lTe8","marks":85},{"name":"C88lI6tE","marks":24},{"name":"Dzq","marks":50},{"name":"jduS","marks":74},{"name":"qvL2LEQ50c","marks":77},{"name":"hKvnGqBau","marks":94},{"name":"xdD","marks":33},{"name":"tymi8p3","marks":82},{"name":"DTdZ","marks":80},{"name":"pjW701","marks":66},{"name":"yUpHIIwK","marks":72},{"name":"HLhZXowh","marks":89},{"name":"lua9iBm7","marks":46},{"name":"nlUBb","marks":36},{"name":"nm","marks":32},{"name":"Dcdg","marks":66},{"name":"ufsoGMP","marks":36},{"name":"D6MYc8K","marks":7},{"name":"fHp7EgvW","marks":65},{"name":"Qw","marks":66},{"name":"Hvt","marks":58},{"name":"WqB7zH","marks":29},{"name":"KC","marks":93},{"name":"LWruUv4YRP","marks":87},{"name":"gya6H3ch","marks":98},{"name":"n","marks":9},{"name":"uPPSz","marks":11},{"name":"G8gm8P","marks":18},{"name":"FlMO","marks":1},{"name":"4nq","marks":34},{"name":"2Avdeoht","marks":96},{"name":"epr","marks":53},{"name":"7vbcE","marks":27},{"name":"Ju","marks":78},{"name":"Kn8oXS7c","marks":30},{"name":"V3yVgga","marks":82},{"name":"BdmsIG","marks":74},{"name":"Tw","marks":73},{"name":"6RG","marks":82},{"name":"CMQyRg","marks":24},{"name":"87","marks":17},{"name":"sI8x7","marks":82},{"name":"5PGM","marks":50},{"name":"rX7aJACLfA","marks":80},{"name":"FtUp4RA","marks":37},{"name":"K90v8","marks":76},{"name":"RAqoU","marks":0},{"name":"ZQpiT","marks":18},{"name":"aI","marks":70},{"name":"SBQzXYmNl","marks":27},{"name":"p","marks":56},{"name":"5PfZp","marks":14}]

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            # Parse query parameters correctly
            query_components = urllib.parse.parse_qs(urllib.parse.urlparse(self.path).query)
            names = query_components.get("name", [])  # Extract list of names
            
            marks_list = []
            
            for name in names:
                student = next((s for s in student_marks if s["name"] == name), None)
                marks_list.append(student["marks"] if student else "Not Found")

            response = {"marks": marks_list}

            # Send JSON response
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            
            # Enable CORS
            self.send_header('Access-Control-Allow-Origin', '*')
            self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS')
            self.send_header('Access-Control-Allow-Headers', 'Content-Type')

            self.end_headers()
            self.wfile.write(json.dumps(response).encode('utf-8'))
        
        except Exception as e:
            # Catch any runtime errors and return a proper error message
            self.send_response(500)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            error_response = {"error": "Internal Server Error", "message": str(e)}
            self.wfile.write(json.dumps(error_response).encode('utf-8'))

    def do_OPTIONS(self):
        # Handle preflight requests for CORS
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()
