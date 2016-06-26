#coding:utf-8
from toughlib import btforms
from toughlib.btforms import rules
from toughlib.btforms.rules import button_style,input_style

boolean = {0:u"否", 1:u"是"}
booleans = {'0': u"否", '1': u"是"}
bool_bypass = {'0': u"免密码认证", '1': u"强制密码认证"}
ra_protocols = {'http': u"HTTP协议", 'zmq': u"ZMQ协议"}

sys_form = btforms.Form(
    btforms.Textbox("system_name", description=u"管理系统名称",help=u"管理系统名称,可以根据你的实际情况进行定制", **input_style),
    btforms.Textbox("system_ticket_expire_days", description=u"上网日志保留天数", **input_style),
    btforms.Button("submit", type="submit", html=u"<b>更新</b>", **button_style),
    title=u"参数配置管理",
    action="/admin/param/update?active=syscfg"
)

notify_form = btforms.Form(
    btforms.Dropdown("expire_notify_enable", args=booleans.items(), description=u"启动到期提醒任务", **input_style),
    btforms.Textbox("expire_notify_days", rules.is_number, description=u"到期提醒提前天数", **input_style),
    btforms.Textbox("expire_notify_interval", rules.is_number, description=u"到期提醒间隔(分钟)", **input_style),
    btforms.Textarea("expire_notify_tpl", description=u"到期提醒邮件模板", rows=5, **input_style),
    btforms.Textbox("expire_notify_url", description=u"到期通知触发URL", **input_style),
    btforms.Textbox("expire_session_timeout", description=u"到期用户下发最大会话时长(秒)", **input_style),
    btforms.Textbox("expire_addrpool", description=u"到期提醒下发地址池", **input_style),
    btforms.Button("submit", type="submit", html=u"<b>更新</b>", **button_style),
    title=u"参数配置管理",
    action="/admin/param/update?active=notifycfg"
)

mail_form = btforms.Form(
    btforms.Textbox("smtp_server", description=u"SMTP服务器", **input_style),
    btforms.Textbox("smtp_port", description=u"SMTP服务器端口", **input_style),
    btforms.Textbox("smtp_from", description=u"SMTP邮件发送地址", **input_style),
    btforms.Textbox("smtp_user", description=u"SMTP用户名", **input_style),
    btforms.Textbox("smtp_pwd", description=u"SMTP密码", help=u"如果密码不是必须的，请填写none", **input_style),
    btforms.Button("submit", type="submit", html=u"<b>更新</b>", **button_style),
    title=u"参数配置管理",
    action="/admin/param/update?active=mailcfg"
)

rad_form = btforms.Form(
    btforms.Dropdown("radius_bypass", args=bool_bypass.items(), description=u"Radius认证模式", **input_style),
    btforms.Textbox("radius_acct_interim_intelval", rules.is_number, description=u"Radius记账间隔(秒)",help=u"radius向bas设备下发的全局记账间隔，bas不支持则不生效", **input_style),
    btforms.Textbox("radius_max_session_timeout", rules.is_number, description=u"Radius最大会话时长(秒)",help=u"用户在线达到最大会话时长时会自动断开", **input_style),
    btforms.Dropdown("radius_auth_auto_unlock", args=booleans.items(), description=u"并发自动解锁", help=u"如果账号被挂死，认证时自动踢下线",**input_style),
    btforms.Button("submit", type="submit", html=u"<b>更新</b>", **button_style),
    title=u"参数配置管理",
    action="/admin/param/update?active=radcfg"
)










