
# API Cronograma Flask

Esse projeto consiste na criação de uma API Rest em Flask que integra um modelo de cronograma de eventos a uma base de dados.


## Documentação da API

### Endpoints de cronogramas
```http
  GET /cronogramas
```
```http
  POST /cronogramas
```
| Parâmetro   | Tipo       |
| :---------- | :--------- |
| `id`      | `int` | 
|`nome`     | `str` |

```http
  GET /cronogramas/${id}
```

```http
  PUT /cronogramas/${id}
```
| Parâmetro   | Tipo       |
| :---------- | :--------- |
| `nome`      | `str` |


```http
  DELETE /cronogramas/${id}
```

### Endpoints de eventos
```http
  GET /eventos
```
```http
  POST /eventos
```
| Parâmetro   | Tipo       |
| :---------- | :--------- |
| `id`      | `int` | 
|`texto`     | `str` |
|`dia`     | `str` |
|`id_cronograma`     | `str` |

```http
  GET /eventos/${id}
```
```http
  PUT /eventos/${id}
```
| Parâmetro   | Tipo       |
| :---------- | :--------- |
|`texto`     | `str` |
|`dia`     | `str` |

```http
  DELETE /eventos/${id}
```