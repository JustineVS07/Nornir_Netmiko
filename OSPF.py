from nornir import InitNornir
from nornir_netmiko import netmiko_send_config
from nornir_jinja2.plugins.tasks import template_file
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")

#nr = nr.filter(platform= "arista_eos")

def OSPF_CONFIG(task):
    if "cisco_xe" in task.host.platform:
        template = "INTERFACE_AND_OSPF_CISCO.j2"
    elif "fortinet" in task.host.platform:
        template = "INTERFACE_AND_OSPF_FORTIGATE.j2"
    elif "arista_eos" in task.host.platform:
        template = "INTERFACE_AND_OSPF_ARISTA.j2"
    else:
        task.results.append("Plataforma no soportada")
        return
    template= task.run(template_file, name="OSPF", template= template, path="PRACTICAS/")
    config_lines = template.result.splitlines()
    task.run(task=netmiko_send_config, name= "send config to devices", config_commands= config_lines)


result = nr.run(task=OSPF_CONFIG)
print_result(result)
