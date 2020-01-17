# Planejar

* Desabilitar o Firewall

Para desabilitar, utilizaria o comando:

```bash
$ sudo ufw disable
```

* Atualizar o serviço de hora

Para isso, precisa instalar o NTP e em seguida, adicionar os servidores que sejam correspondentes a área para atualização do horário. E enfim, precisa-se iniciar o serviço NTPD.

```bash
$ sudo apt-get install ntp
```

```bash
$ sudo ntpdate -s time.nist.gov
```

```bash
$ sudo service ntp start
```

* Atualizar o sistema operacional - Ubuntu

```bash
$ sudo apt-get update && sudo apt-get upgrade
```

* Instalar o servidor Docker

```bash
$ sudo apt-get install docker
```