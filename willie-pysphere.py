from willie.module import commands
from pysphere import VIServer


def _check_config(bot):
    if not bot.config.has_option('pysphere', 'server'):
        bot.say("You need to configure server")
        return False
    if not bot.config.has_option('pysphere', 'login'):
        bot.say("You need to configure login")
        return False
    if not bot.config.has_option('pysphere', 'password'):
        bot.say("You need to configure password")
        return False
    else:
        return True

def _connect_server(bot):
    try:
        server = VIServer()
        server.connect(bot.config.pysphere.server, bot.config.pysphere.login, bot.config.pysphere.password)        
    except Exception, e:
        return False
    return server

@commands('vmlist')
def vmlist(bot, trigger):
    config = _check_config(bot)
    if config == False:
        return
    server = _connect_server(bot)
    vmlist = server.get_registered_vms()

    if len(vmlist) == 0:
        bot.say("No machines here!")
        return
    else:
        bot.say("Currently "+ str(len(vmlist)) + " machines are running. I will spam them now.")
        for vm in vmlist:
            bot.say(vm +" " + server.get_vm_by_path(vm).get_status())
        bot.say("Thats all machines and their status")

@commands('vmpoweron')
def vmpoweron(bot, trigger):
    config = _check_config(bot)
    if config == False:
        return
    server = _connect_server(bot)

    try:
        vm = server.get_vm_by_path(trigger.group(2))
        vm.power_on()
        bot.say(trigger.nick + ": powering on " + trigger.group(2))
        pass
    except Exception, e:
        bot.say(trigger.nick + ": you are drunken. Please give me a proper machine name!")
        print e

@commands('vmpoweroff')
def vmpoweroff(bot, trigger):
    config = _check_config(bot)
    if config == False:
        return
    server = _connect_server(bot)

    try:
        vm = server.get_vm_by_path(trigger.group(2))
        vm.power_off()
        bot.say(trigger.nick + ": powering down " + trigger.group(2))
        pass
    except Exception, e:
        bot.say(trigger.nick + ": you are drunken. Please give me a proper machine name!")
        print e
