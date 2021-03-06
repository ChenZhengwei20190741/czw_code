# -*- coding: utf-8 -*-

import time
import pywifi

connect_status = {
    0: 'DISCONNECTED',
    1: 'SCANNING',
    2: 'INACTIVE',
    3: 'CONNECTING',
    4: 'CONNECTED',
}


class WifiDriver(object):

    def __init__(self, config):
        self.wifi = pywifi.PyWiFi()
        # choose wifi interface
        self.iface = self.wifi.interfaces()[0]

        self.profile = pywifi.Profile()
        self._ini_profile(wifi_profile=config)

    def _ini_profile(self, wifi_profile):
        """初始化profile文件
        :param wifi_profile: wifi参数，dict
        """

        # wifi名称
        self.profile.ssid = wifi_profile['ssid']
        # 需要密码
        self.profile.auth = wifi_profile['auth']
        # 加密类型
        self.profile.akm.append(wifi_profile['akm'])
        # 加密单元
        self.profile.cipher = wifi_profile['cipher']
        # wifi密码
        self.profile.key = wifi_profile['key']

    def remove_all_network(self):
        """清除所有网络连接"""
        self.iface.remove_all_network_profiles()

    def connect_network(self):
        """连接网络"""
        temp_profile = self.iface.add_network_profile(self.profile)
        self.iface.connect(temp_profile)

    def disconnect_network(self):
        """断开网络连接"""
        self.iface.disconnect()

    def network_status(self):
        """返回网络状态"""
        return self.iface.status()

    def scan_wifi(self, timeout=10):
        """扫描可用wifi"""
        ssid_l = []
        print('start to scan ssid, wait {}s'.format(timeout))
        self.iface.scan()
        time.sleep(timeout)
        result = self.iface.scan_results()
        if result is not None:
            for profile in result:
                ssid = profile.ssid
                ssid_l.append(ssid)
        print('ssid:{}'.format(set(ssid_l)))
        return set(ssid_l)


if __name__ == '__main__':
    wifi_conf = {
        'ssid': 'CZWWORK_2.4G',
        'auth': pywifi.const.AUTH_ALG_OPEN,
        'akm': pywifi.const.AKM_TYPE_WPA2PSK,
        'cipher': pywifi.const.CIPHER_TYPE_CCMP,
        'key': '12345678'}

    wifi_instance = WifiDriver(wifi_conf)

    wifi_instance.scan_wifi()

    wifi_instance.remove_all_network()
    time.sleep(1)

    wifi_instance.connect_network()
    for i in range(10):
        print('等待{}s, wifi status is {}'.format(i+1, connect_status[wifi_instance.network_status()]))
        if wifi_instance.network_status() == 4:
            print('wifi连接成功')
            break
        time.sleep(1)

    wifi_instance.disconnect_network()
    for i in range(10):
        print('等待{}s, wifi status is {}'.format(i+1, connect_status[wifi_instance.network_status()]))
        if wifi_instance.network_status() == 0:
            print('断开wifi连接成功')
            break
        time.sleep(1)
