
# API Cronograma Flask

Esse projeto consiste na criação de uma API Rest em Flask que integra um modelo de cronograma de eventos a uma base de dados.


## Documentação da API

### Endpoints de cronogramas
```http
  GET /cronogramas
```
```http
  GET /cronogramas/${id}
```
```http
  POST /cronogramas
```
| Parâmetro   | Tipo       |
| :---------- | :--------- |
| `id`      | `int` | 
|`nome`     | `str` |

```http
  PUT /cronogramas/${id}
```
| Parâmetro   | Tipo       |
| :---------- | :--------- |
| `nome`      | `str` |


```http
  DELETE /cronogramas/${id}
```