from nornir import InitNornir
from nornir_netmiko import netmiko_send_config
from nornir_jinja2.plugins.tasks import template_file
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file=r"F:\NETWORKING\Automation and Programming\VSCode\Learning Python\Nornir Automation\Static_Route and ACL\config.yaml")

nr = nr.filter(platform="fortinet") # Para filtrar si queremos aplicar el codigo a los equipos con platform fortinet.

def Static_Route_ACL(task):
    if "cisco_xe" in task.host.platform:
        template = "StaticRoute_ACL_CISCO.j2"
    elif "fortinet" in task.host.platform:
        template = "StaticRoute_ACL_FORTI.j2"
    else:
        task.results.append("Plataforma no soportada")
        return
    template= task.run(template_file, name="StaticRoute", template= template, path="Static_Route and ACL/")
    config_lines = template.result.splitlines()
    task.run(task=netmiko_send_config, name= "send config to devices", config_commands= config_lines)


result = nr.run(task=Static_Route_ACL)
print_result(result)