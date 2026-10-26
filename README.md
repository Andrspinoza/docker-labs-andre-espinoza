# docker labs - andré espinoza

proyecto práctico de dockerfile y construcción de imágenes (bootcamp devops tecsup g5).

| lab | carpeta | imagen | puerto |
|---|---|---|---|
| 01 | [01-nginx-basico](01-nginx-basico) | `andre-espinoza-web:v1` | 8080 -> 80 |
| 02 | [02-api-python](02-api-python) | `andre-espinoza-api:v1` | 8081 -> 8000 |
| 03 | [03-optimizacion](03-optimizacion) | `andre-espinoza-api:v2` | 8082 -> 8000 |
| 04 | [04-seguridad](04-seguridad) | `andre-espinoza-api:v3` | 8083 -> 8000 |

todo se probó en local con docker desktop. cada carpeta tiene su dockerfile, su readme y sus capturas en `evidencias/`.
no hay contraseñas ni archivos `.env` en el repo.