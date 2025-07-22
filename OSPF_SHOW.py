from nornir import InitNornir
from nornir_netmiko import netmiko_send_command
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file=r"F:\NETWORKING\Automation and Programming\VSCode\Learning Python\Nornir Automation\PRACTICAS\config.yaml")

# nr = nr.filter(platform= "arista_eos")
def OSPF_SHOW(task):
    if "cisco_xe" in task.host.platform:
        show = "show ip ospf neigh"
    elif "fortinet" in task.host.platform:
        show = "get router info ospf neighbor"
    elif "arista_eos" in task.host.platform:
        show = "show ip ospf neigh"
    else:
        task.results.append("Plataforma no soportada")
        return
    
    task.run(task=netmiko_send_command, name= "send show command", command_string= show)


result = nr.run(task=OSPF_SHOW)
print_result(result)

