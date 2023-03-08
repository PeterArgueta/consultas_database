import json

ID=json.load(open('stationsname.txt'))
directory="outputhtml/"

for k in ID: 
        html = '''
        <!DOCTYPE html>
        <meta charset="UTF-8">
        <html lang="en">
        <head>
        <title>Datos mensuales</title>
        </head>
        <body>
        <style>
            /* Estilos para la tabla */
            table {
            border-collapse: collapse;
            width: 80%;
            max-width: 1200px;
            margin: 0 auto;
            }
            table th,
            table td {
            border: 1px solid #ccc;
            padding: 5px;
            text-align: center;
            }
            table th:first-child,
            table td:first-child {
            width: 100px;
            }
            table th {
            background-color: #0074D9;
            color: white;
            text-align: center;
            font-weight: bold;
            }
            /* Estilos para el botón de descarga */
            button {
            background-color: #0074D9;
            color: white;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            padding: 10px 20px;
            font-size: 16px;
            display: block;
            margin: 20px auto 0;
            }
            button:hover {
            background-color: #005ca9;
            }
        </style>
        <h1>ESTACIÓN '''+k+''' </h1>
        <script type="text/javascript">
            function processData(csv) {
            let data = csv.split(/\\r|\\n/).map(v => v.split(','));
            let headers = data.shift();
            let table = document.createElement('table');
            let thead = document.createElement('thead');
            table.appendChild(thead);
            thead.innerHTML = '<tr><th>' + headers.join('</th><th>') + '</th></tr>';
            let tbody = document.createElement('tbody');
            table.appendChild(tbody);
            for (let row of data) {
                tbody.innerHTML += '<tr><td>' + row.join('</td><td>') + '</td></tr>';
            }
            document.body.appendChild(table);
            // Add download button
            const csvData = headers.join(",") + "," + data.map(row => row.join(",")).join("\\n");
            const downloadButton = document.createElement('button');
            downloadButton.innerHTML = 'Download as CSV';
            downloadButton.onclick = function() {
                const blob = new Blob([csvData], {type: 'text/csv'});
                const url = window.URL.createObjectURL(blob);
                const a = document.createElement('a');
                a.setAttribute('href', url);
                a.setAttribute('download', 'Data_mensual_'''+k+'''.csv');
                document.body.appendChild(a);
                a.click();
                document.body.removeChild(a);
                window.URL.revokeObjectURL(url);
            };
            document.body.appendChild(downloadButton);
            }
            // Fetch the CSV file and process it
            fetch("https://raw.githubusercontent.com/PeterArgueta/consultas_database/master/outputcsv/'''+k+'''.csv")
            .then(res => res.text())
            .then(text => processData(text));
        </script>
        </body>
        </html>
        '''

    # Imprimir el código HTML

        with open(f'{directory}{k}.html', 'w') as f:
            f.write(html)

