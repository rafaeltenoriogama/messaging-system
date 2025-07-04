# Basic Grafana UI config

- Added Zabbix plugin
- Go to 'Data Sources' added 'alexanderzobnin-zabbix-datasource'
- The URL can be either '<http://zabbix-web:8080/api_jsonrpc.php>' or '<http://localhost:8080/api_jsonrpc.php>'
- The 'Authentication' need to be define at 'Zabbix Connection' (leave as \*No authentication) and put the default login of Zabbix.
- Save & Test

# Basic Zabbix Server dashboard

- Go to 'Dashboards'
- Search by 'Zabbix' or 'Kafka' on the [Oficial Grafana Website](https://grafana.com/grafana/dashboards)
- Copy ID to clipboard and use on your Grafana server by the "Import Dashboard".
