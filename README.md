# ETL / ELT Pipeline with dbt, Snowflake and Airflow

## 1. Project Overview
Este proyecto consiste en construir un pipeline moderno de datos orientado a analítica para un negocio de e-commerce.  
El flujo comienza con la llegada de archivos de datos a AWS S3, continúa con la orquestación en Apache Airflow, la carga de datos crudos a Snowflake y la transformación analítica con dbt.  
El objetivo es simular un entorno real de Analytics Engineering, aplicando buenas prácticas de modelado por capas, pruebas de calidad y monitoreo automático.  
Al finalizar, el proyecto permitirá generar modelos analíticos confiables sobre ventas, clientes, productos y pagos, listos para ser consumidos por analistas o herramientas de BI.

## 2. Business Goal
El objetivo de negocio es centralizar y transformar datos operativos de e-commerce para responder preguntas analíticas como:

- ¿Cuánto vende el negocio por día, semana y mes?
- ¿Qué productos generan más ingresos?
- ¿Qué clientes compran con mayor frecuencia?
- ¿Cuál es la tasa de pago exitoso vs pago fallido?
- ¿Cuál es el ticket promedio por orden?

Este pipeline busca convertir datos crudos en información confiable para la toma de decisiones, reduciendo trabajo manual y mejorando la calidad de los datos.

## 3. Proposed Architecture
S3 -> Airflow -> Snowflake -> dbt -> Slack

### Architecture Description
- **AWS S3** almacenará los archivos de entrada en formato CSV.
- **Apache Airflow** detectará nuevos archivos y orquestará la ejecución del pipeline.
- **Snowflake** funcionará como data warehouse para almacenar datos raw y transformados.
- **dbt** se encargará de transformar los datos dentro de Snowflake usando un enfoque ELT.
- **Slack** recibirá alertas de éxito o fallo del pipeline.

## 4. Data Scope
El proyecto trabajará con un dominio de e-commerce y tendrá las siguientes entidades base:

- **customers**: información de clientes
- **products**: catálogo de productos
- **orders**: órdenes realizadas
- **order_items**: detalle de productos por orden
- **payments**: información de pagos asociados a las órdenes

### Expected Raw Tables
- raw_customers
- raw_products
- raw_orders
- raw_order_items
- raw_payments

## 5. Transformation Layers

### staging
En esta capa se limpiarán y estandarizarán los datos crudos:
- renombrado de columnas
- tipado de datos
- normalización de valores nulos
- estandarización de fechas y claves
- eliminación de inconsistencias evidentes

Ejemplos:
- `stg_customers`
- `stg_products`
- `stg_orders`
- `stg_order_items`
- `stg_payments`

### intermediate
En esta capa se construirá la lógica intermedia del negocio:
- joins entre órdenes, clientes, productos y pagos
- cálculo de subtotales por orden
- enriquecimiento de órdenes con estado de pago
- preparación de datasets reutilizables para métricas

Ejemplos:
- `int_orders_enriched`
- `int_order_items_enriched`
- `int_payments_summary`

### marts
En esta capa se expondrán modelos analíticos finales listos para consumo:
- métricas de ventas
- desempeño de productos
- comportamiento de clientes
- indicadores de pago

Ejemplos:
- `fct_orders`
- `fct_sales`
- `dim_customers`
- `dim_products`
- `mart_daily_sales`

## 6. Orchestration Flow
El DAG de Airflow seguirá este flujo:

1. Esperar la llegada de nuevos archivos a un bucket/prefix de S3.
2. Validar que el archivo esperado exista.
3. Cargar los datos raw desde S3 hacia Snowflake.
4. Ejecutar `dbt run` para construir las capas de transformación.
5. Ejecutar `dbt test` para validar calidad de datos.
6. Enviar una notificación a Slack indicando éxito o fallo del pipeline.

## 7. Project Deliverables
Al finalizar el proyecto, deberán existir los siguientes entregables:

- Un DAG funcional en Airflow
- Carga de datos raw desde S3 hacia Snowflake
- Proyecto dbt configurado y conectado a Snowflake
- Modelos organizados en capas: `staging`, `intermediate`, `marts`
- Tests de calidad en dbt
- Notificaciones automáticas a Slack
- Estructura de repositorio profesional en GitHub
- README completo con arquitectura, decisiones y pasos de ejecución
- Evidencia visual del proyecto funcionando (capturas o demo)

## 8. Success Criteria
El proyecto se considerará terminado cuando cumpla con todos los siguientes criterios:

- Airflow detecta automáticamente la llegada de nuevos archivos en S3.
- Los archivos se cargan correctamente a tablas raw en Snowflake.
- dbt ejecuta exitosamente los modelos de `staging`, `intermediate` y `marts`.
- Los tests de dbt validan calidad mínima de datos sin errores críticos.
- Slack recibe alertas al finalizar la ejecución del pipeline.
- El repositorio puede ser entendido y ejecutado por otra persona siguiendo el README.
- El proyecto tiene calidad suficiente para mostrarse como pieza de portafolio profesional.

## 9. Tech Stack
- **Orchestration:** Apache Airflow
- **Data Warehouse:** Snowflake
- **Transformations:** dbt
- **Cloud Storage:** AWS S3
- **Compute/Deployment:** AWS EC2
- **Monitoring/Alerts:** Slack

## 10. Portfolio Value
Este proyecto demuestra habilidades clave de Ingeniería de Datos y Analytics Engineering:

- diseño de pipelines ELT modernos
- orquestación de flujos de datos
- modelado analítico por capas
- automatización de validaciones de calidad
- observabilidad y alertamiento
- documentación técnica y buenas prácticas de portafolio

## 11. Entorno de desarrollo

Este proyecto utilizará la siguiente estrategia de desarrollo:

- **Apache Airflow** se ejecutará localmente con Docker.
- **dbt** se configurará dentro del proyecto y se conectará a Snowflake.
- **Snowflake** se utilizará como el data warehouse en la nube.
- **AWS S3** se utilizará como la zona de aterrizaje de datos en bruto.
- **Slack** se utilizará para las notificaciones del pipeline.
- Las variables de entorno se gestionarán mediante un archivo local .env basado en .env.example.

### Variables de entorno requeridas
El proyecto requiere credenciales y configuración para:
- Conexión a Snowflake
- Acceso a AWS y bucket de S3
- Notificaciones por webhook de Slack
- Entorno local de Airflow
