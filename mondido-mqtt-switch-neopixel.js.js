// var client  = mqtt.connect({ host:'test.mosquitto.org', port: 8081})
// or
// var client  = mqtt.connect('wss://test.mosquitto.org:8081/mqtt')

// var client  = mqtt.connect({ host:'mqtt.eclipse.org/mqtt', port: 443})
// or
// var client  = mqtt.connect('wss://mqtt.eclipse.org:443/mqtt')

var client = mqtt.connect('wss://mqtt.eclipseprojects.io:443/mqtt')
// var client  = mqtt.connect(broker);

var status_header = document.getElementById('status-header')

client.on('connect', function () {
    status_header.innerHTML = 'Connected to '+broker; 
    console.log('Connected to '+broker)
})

var pub_switch = document.getElementById('pub-switch');
pub_switch.onclick = () => {
    console.log(pub_switch.checked)
    client.publish('cpx-switch/pub_switch', String(pub_switch.checked))
}

var pub_switch2 = document.getElementById('pub-switch2');
pub_switch2.onclick = () => {
    console.log(pub_switch2.checked)
    client.publish('cpx-switch/pub_switch2', String(pub_switch2.checked))
}
var pub_switch3 = document.getElementById('pub-switch3');
pub_switch3.onclick = () => {
    console.log(pub_switch3.checked)
    client.publish('cpx-switch/pub_switch3', String(pub_switch3.checked))
}

