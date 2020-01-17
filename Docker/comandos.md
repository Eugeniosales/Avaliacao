## Comandos Docker

* Verficar quais conteiners estão rodando

```bash
$ sudo docker ps
```

* Verificar quais conteiners estão parados

```bash
$ sudo docker ps -a
```

* Verificar quais os volumes existentes

```bash
$ sudo docker volume ls
```

* Excluir apenas os conteiners parados

```bash
$ sudo docker rm $(docker container ls –aq)
```

* Excluir apenas os volumes não utilizados

```bash
$ sudo docker volume prune
```

* Criar um volume com o nome volume-meu-primeiro-nome

```bash
$ sudo docker volume create eugenio
```