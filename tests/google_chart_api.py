from string import Template
from itertools import chain
from datetime import date
from tests.read_in_data import read_in_data_test_timing_data, read_in_data_test_analysis_data
from tests.analyze_jira_data import analyze_jira_data_test


class global_variables:

    html_string = Template("""<html>
            <head>
            <script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
            <script type="text/javascript">
              google.charts.load('current', {packages: ['corechart']});
              google.charts.setOnLoadCallback(drawChart);
              function drawChart () {
                  var data = new google.visualization.DataTable();
                  data.addColumn('string');
                  data.addColumn('number', '$label_one');
                  if("$label_two" != "null"){
                  data.addColumn('number', '$label_two');
                  }
                  
                  data.addRows([
                    $data
                  ]);
                var chart = new google.visualization.ColumnChart(document.getElementById('chart_div'));
                  chart.draw(data);
              }
            </script>
            </head>
            <body>
            <div id="chart_div" style="width:1100; height:680"></div>
            </body>
            </html>""")

    html_string_pie = Template("""
    <html>
      <head>
        <script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
        <script type="text/javascript">
          google.charts.load('current', {'packages':['corechart']});
          google.charts.setOnLoadCallback(drawChart);
    
          function drawChart() {
    
            var data = google.visualization.arrayToDataTable([
              ['Status', 'Number of Issues'],
               $status_data_in
            ]);
    
            var options = {
              title: 'Issues By Status'
            };
    
            var chart = new google.visualization.PieChart(document.getElementById('piechart'));
    
            chart.draw(data, options);
          }
        </script>
      </head>
      <body>
        <div id="piechart" style="width: 900px; height: 500px;"></div>
      </body>
    </html>
    """)


class google_chart_api_test_timing_data:

    def start(self):

        timing_chart_data = read_in_data_test_timing_data().start()

        chart_data_str = ''
        for row in timing_chart_data[1:]:
            chart_data_str += '%s,\n' % row

        completed_html = global_variables.html_string.substitute(label_one=timing_chart_data[0][1],
                                                                label_two="null",
                                                                data=chart_data_str)
        file_date = date.today()
        with open('tests/test_docs/charts/timing_chart_'+str(file_date)+'.html', 'w') as f:
            f.write(completed_html)
    pass


class google_chart_api_test_analysis_data:

    def start(self):

        analysis_chart_data = read_in_data_test_analysis_data().start()

        chart_data_str = ''
        for row in analysis_chart_data[1:]:
            chart_data_str += '%s,\n' % row

        # join_analysis_chart_data = ('\',\''.join(analysis_chart_data[0][1:]))
        completed_html = global_variables.html_string.substitute(label_one=analysis_chart_data[0][1],
                                                                label_two=analysis_chart_data[0][2],
                                                                data=chart_data_str)
        file_date = date.today()
        with open('tests/test_docs/charts/analysis_chart_' + str(file_date) + '.html', 'w') as f:
            f.write(completed_html)
    pass

class google_chart_api_test_jira_data:

    def start(self):
        status_data = analyze_jira_data_test().start()

        formatted_data = ''
        for stat in status_data.keys():
            formatted_data += "['%s', %s],\n" % (stat, status_data[stat])

        print(formatted_data)

        completed_html = global_variables.html_string_pie.substitute(status_data_in=formatted_data)

        file_date = date.today()
        with open('tests/test_docs/charts/status_pie_chart_' + str(file_date) + '.html', 'w') as f:
            f.write(completed_html)
