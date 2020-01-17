# Playbook

* Desabilitar o Firewall

```bash
$ sudo ufw disable
```

* Iniciar o NTPD

```bash
$ service ntpd start
```

* Criar um grupo de nome poupex

```bash
$ sudo groupadd poupex
```

* Criar um usuário de nome devops ao qual faz parte do grupo poupex

```bash
$ sudo useradd devops
```

```bash
$ sudo usermod -G poupex devops
```