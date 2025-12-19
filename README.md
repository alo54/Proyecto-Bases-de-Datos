# Proyecto: Análisis de accidentes de tráfico en Chicago

## Integrantes
- Regina Cabral
- Alondra Valdivia
- Gabriel Navarro
- Iker Navarro
- Ricardo Limón

## Descripción general 

El conjunto de datos de “Accidentes de Tráfico de Chicago” es un registro público que contiene información detallada de cada choque reportable dentro de los límites de la ciudad y bajo la jurisdicción del Departamento de Policía de Chicago (CPD). Incluye circunstancias, causas y consecuencias de los incidentes viales, desde daños materiales menores hasta colisiones fatales.

Para este proyecto se usarán los datasets públicos: **Traffic Crashes - Crashes**, **Traffic Crashes - Vehicles** y **Traffic Crashes - People**, obtenidos del [Chicago Open Data Portal](https://data.cityofchicago.org/).  

Los datos son recolectados diariamente por el CPD a través del sistema **E-Crash**, con el objetivo de mantener registros oficiales, apoyar iniciativas de seguridad pública y permitir al Departamento de Transporte de Chicago (CDOT) identificar áreas de riesgo y evaluar proyectos de seguridad vial.

**Enlaces a los datasets:**
- [Crashes](https://data.cityofchicago.org/Transportation/Traffic-Crashes-Crashes/85ca-t3if/about_data)  
- [Vehicles](https://data.cityofchicago.org/Transportation/Traffic-Crashes-Vehicles/68nd-jvt3/about_data)  
- [People](https://data.cityofchicago.org/Transportation/Traffic-Crashes-People/u6pd-qa9d/about_data)  

---

## Resumen de datos

| Dataset | Tuplas | Atributos |
|:-------:|:------:|:---------:|
| Crashes | 989,000 | 48 |
| Vehicles | 2,020,000 | 71 |
| People | 2,170,000 | 29 |

> El conjunto solo incluye choques donde el CPD fue la agencia respondedora; accidentes en autopistas interestatales y algunas carreteras limítrofes están excluidos.

---

## Atributos 

### Traffic Crashes - Crashes

| Atributo | Tipo | Descripción |
|:---------|:----:|:-----------|
| crash_record_id | Texto | Identificador único del accidente |
| crash_date | Fecha/Hora | Fecha y hora del accidente |
| crash_hour | Numérico | Hora del accidente |
| crash_day_of_week | Numérico | Día de la semana (1=domingo) |
| crash_month | Numérico | Mes del accidente |
| posted_speed_limit | Numérico | Límite de velocidad |
| lane_cnt | Numérico | Número de carriles |
| traffic_control_device | Categórico | Dispositivo de control de tráfico |
| device_condition | Categórico | Estado del dispositivo |
| weather_condition | Categórico | Condiciones climáticas |
| lighting_condition | Categórico | Condiciones de iluminación |
| first_crash_type | Categórico | Tipo de primera colisión |
| crash_type | Categórico | Severidad general del accidente |
| prim_contributory_cause | Categórico | Causa primaria del accidente |
| sec_contributory_cause | Categórico | Causa secundaria |
| latitude / longitude | Numérico | Coordenadas geográficas |
| street_name / street_no / street_direction | Texto | Dirección del accidente |
| num_units | Numérico | Número de unidades involucradas |
| injuries_total / fatal / incapacitating / non_incapacitating / no_indication / unknown | Numérico | Total y tipo de lesiones |
| most_severe_injury | Categórico | Lesión más grave observada |
| report_type | Texto | Tipo de reporte administrativo |
| photos_taken_i / statements_taken_i / dooring_i / work_zone_i / workers_present_i | Categórico | Indicadores de observación |

---

### Traffic Crashes - Vehicles

| Atributo | Tipo | Descripción |
|:---------|:----:|:-----------|
| crash_record_id | Texto | Relaciona con Crashes |
| vehicle_id / crash_unit_id / unit_no | Numérico | Identificadores de vehículo |
| vehicle_type / make / model | Categórico | Tipo, marca y modelo |
| vehicle_year | Numérico | Año del modelo |
| occupant_cnt / num_passengers | Numérico | Cantidad de ocupantes |
| unit_type / maneuver / travel_direction / towed_i / fire_i / exceed_speed_limit_i | Categórico | Características y condiciones del vehículo |
| cargo_body_type / load_type / hazmat_present_i | Categórico | Información de carga y materiales peligrosos |
| crash_date | Fecha/Hora | Fecha y hora del accidente |

---

### Traffic Crashes - People

| Atributo | Tipo | Descripción |
|:---------|:----:|:-----------|
| person_id | Texto | Identificador de la persona (P=pasajero, O=otro) |
| crash_record_id | Texto | Relaciona con Crashes |
| vehicle_id | Texto | Relaciona con Vehicles |
| person_type | Categórico | Conductor, pasajero, peatón o ciclista |
| age | Numérico | Edad de la persona |
| sex | Categórico | Género |
| seat_no | Categórico | Posición en el vehículo |
| drivers_license_state / drivers_license_class | Categórico | Información de licencia de conducir |
| safety_equipment / airbag_deployed / ejection | Categórico | Equipo de seguridad y resultados del accidente |
| injury_classification | Categórico | Severidad de lesión |
| hospital / ems_agency / ems_run_no | Texto | Atención médica y transporte |
| driver_action / driver_vision / physical_condition | Categórico | Comportamiento y condición del conductor |
| pedpedal_action / pedpedal_visibility / pedpedal_location | Categórico | Acción y ubicación de peatón/ciclista |
| bac_result / bac_result_value | Categórico / Numérico | Prueba de alcohol en sangre |
| cell_phone_use | Categórico | Uso de celular al momento del accidente |
| crash_date | Fecha/Hora | Fecha y hora del accidente |

---

## Objetivo del Proyecto

El objetivo del análisis es identificar **factores de riesgo** y **patrones de accidentes** para proponer medidas que mejoren la seguridad vial.  

**Enfoques posibles:**
- **Seguridad Vial:** Analizar clima, hora, tipo de vehículo y condiciones de la vía sobre la severidad de lesiones.  
- **Espacial:** Identificar calles e intersecciones con mayor concentración de accidentes (*hotspots*).  
- **Temporal:** Detectar tendencias por hora, día de la semana y estación del año.  
- **Comportamiento de Conductores:** Evaluar infracciones, distracciones y consumo de alcohol.  
- **Multidimensional:** Cruzar atributos como tipo de vehículo, hora y clima para análisis más completos.

---

## Consideraciones Éticas

- **Protección de la Privacidad:** El dataset está anonimizado. No se deben intentar re-identificar personas.  
- **Precisión y Limitaciones:** Los datos pueden contener errores o sesgos; el análisis debe considerarlos.  
- **Equidad y Desigualdad Social:** Las fatalidades no se distribuyen uniformemente; se debe tener cuidado de no reforzar prejuicios.  
- **Comunicación Responsable:** Presentar hallazgos con contexto; un alto número de accidentes puede reflejar mayor tráfico y no necesariamente un diseño peligroso de la vía.

---
## Limpieza de datos
El proceso de limpieza de datos se realizó de manera incremental y sistemática sobre cada una de las tablas creadas, con el objetivo de garantizar consistencis, eliminar valores inválidos y estandarizar los formatos antes de realizar análisis o consultas complejas. 

Uno de los principales problemas detectados fue a presencia de valores nulos no explícitos, es decir, cadenas vacias (`''`) o valores de texto que representaban auencia de información. Para solucionarlo, se aplicaron funciones como `NULLIF`, `BTRIM`  y `COALESCE`, tranformando estos registros en valores `NULL` reales dentro de PostgresSQL.

En la tabla **`people`** se normalizaron atributos como **`people_type`**, **`sex`**, **`safety_equipment`**,**`airbag_deployed`** e **`injuty_classification`**, eliminando cadenas vacías y estandarizando los valoes. De manera similar en la tabla **`vehicle`** se limpiaron campos textuales como **`unit_type`**, **`make`**, **`model`** y **`vehice_type`**.

Para las tablas especializdas de vehiculos (**`vehicle_models`**, **`vehicle_maneuvers`**, **`vehicle_violations`**) se aplicaron transformaciones adicionales para eliminar espacios innecesarios y corregir valores inválidos, garantizando que los atributos categóricos fueran consistentes y tulizables en análisis posteriores. 

En el caso de **`drive_info`**, se realizó una limpieza más exhaustiva debido a la gran diversidad de valores en atributos como **`driver_action`**, **`driver_vision`**, **`physical?condition`** y **`druvers_license_class`**. Se eliminaron caracteres no válidos, se estandarizó el uso de mayúsculas y se validaron expresiones mediante expresiones regulares para asegurar la coherencia de los registros. 

Por último, en **`crash_injuries`** se detectó la presencia de valores nulo en campos númericos críticos. Para evitar incosistencias en los cálculos agregados, estos calores se sustituyeron por ceros utilizando **`COALESCE`**, bajo el supuesto de que la ausencia de registrosimplicaba la inexistencia de lesiones de ese tipo. 

Al concluir este proceso, se obtuvo un conjunto de tablas con datos limpios, tipados correctamente y coherente entre sí, litos para su análisis y para garantizar integridad durante la normalización. 

---
## Normalización de datos

La estructura final del modelos de datos refleja un proceso de normalizaciòn que alcanza tercera forma nomal (3FN), e incluo se aproxima a BCNF, al eliminar redundancias y asegurar que cada atributo depende únicamente de la llave primario de su tabla. 

Cada tabla representa una entidad claramente definida: 
- Crashes: información base del accidente.
- Crash_date, cras_circumstances, crash_injuries, crash_classification: descomposición funcional del accidente en subconjuntos lógicos de atributos.
- Vehicle y sus tablas asociadas: modelan de forma independiente a cada vehículo involucrado.
- People y driver_info: separan información genral de personas de informacion exclusiva de conductores.

Las dependenciasfuncionales principales observadas incluyen: 
- `{crash_record_id} →` atributos del accidente y sus subcomponentes.
- `{vehicle_id} →` atributos propios del vehículo
- `{person_id} →` atributos personales y, en el caso de conductores, atributos específicos de conducción.

La separación de información permitió eliminar duplicidad de datos, reducir anomalías de actualización y facilitar la extensión futura del modelo. El uso de llaves foráneas asegura integridad referencial entre las entidades, mientras que la ausencia de dependencias parciale so transitivas en las tablas confirma el cumplimiento de los criterios de normalización establecidos. 

Como resultado, se obtuvo un esquema relacional robusto, flexible y alineado con las mejores prácticas de diseño de base de datos relacionales para análisis de eventos complejos como accidentes de tráncito. 

<img width="1280" height="498" alt="image" src="https://github.com/user-attachments/assets/444a6459-e7e1-4ab1-b94a-f8076b2957bf" />

## Carga inicial de datos y analisis preliminar

Para la carga inicial de datos se deicidio utilizar un enfoque en el cual la información original del conjunto de datos de accidentes de tránsito se separó desde un inicio en múltiples tablas relaciondas. Esta decision se tomó debido a la alta heterogeneidad de los atributos y a la clara existencia de entidades conceptuales distintas, como accidentes, vehículos y personas involucradas. 

El proceso comenzó con la creación de la tabla principal **'crashes'**, la cual concentra la información base de cada accidente, identificada de manera única por el etributo **'crash_record_id'**. Esta tabla almacena información temporal y espacial del evento, como la fecha del accidente, coordenadas geográficas y la vialidad asociada. 

Posteriormente, a partir del identificados del accidente, se crearon tablas auxiliares especializdas que capturan distinos aspectos del mismo evento: 
-**'crash_date'**, que descompone la fecha del accidente en día de la semana y mes facilitando análisis temporales. 
-**'crash_circumstances'**, que almacena condiciones del entorno vial y del accidente (dispositivos de control de tráfico, clima, iluminación, número de carriles, velocidad permitida, etc.).
-**'crash_injuties'**, que concentra la información relacionada con lesiones resultantes del accidente.
-**'crash_classification'**, que clasifica el tipo de choque, causas contribuyentes y si se trató de un evento de tipo hit-and-run

Todas estas tablas mantienen una relación uno a uno con la tabla **'crashes'** mediante el uso de llaves foráneas sobre **'crash_record_id'**, garantizando coherencia referencial desde la etapa inicial de carga. 

De forma análoga, se creó la entidad **'vehicle'**, que representa a cada vehículo involucrado en un accidente. Cadavehículo se identiica mediante **'vehicle_id'** y se relaciona con un acciednte específico a través de **'crash_record_id'**. A partir de esta tabla se derivaron estructuras adicionales para capturar características específicas:
-**'vehicle_models'**, para información estructural del vehículo.
-**'vehicle_maneuvers'**, para registrar la maniobra realizada al momento del accidente. 
-**'vehicle_violations'**, que indica infracciones o condiciones especiales del vehículo. 

Finalmente, se creó la tabla **'people'**, que contiene la información de las personas involucradas en los accidentes, junto con la tabla **'driver_info'**, que especializa la infomación únicamnete para aquellas personas que actuaban como conductores. Estas tablas se relacionan tanto con **'crashes'** como con **'vehicle'**, permitiendo modelar adecuadamente la participación de cada individuo en el evento. 

Este diseño inicial permitió contar desde el incio con una base de datos estructurada, coherente y preparada para un proceso sistemático de limpieza y normalización

---
## Limpieza y Normalización de datos

## Análisis de datos a través de consultas SQL
Realizamos varias consultas de SQL para el análisis de la base de datos, descubriendo información valiosa para identificar y concluir acerca de factores de riesgo y patrones de accidentes 

### I. Condiciones viales
1. Accidentes por defectos de la vía (road deffects)

```sql
SELECT
    cc.road_defect,
    COUNT(DISTINCT c.crash_record_id) AS total_crashes
FROM crashes c
JOIN crash_circumstances cc
    ON c.crash_record_id = cc.crash_record_id
WHERE cc.road_defect IS NOT NULL
GROUP BY cc.road_defect
ORDER BY total_crashes DESC;
```

2. Calles con más accidentes

```sql
SELECT
    c.street_name,
    COUNT(*) AS total_crashes
FROM CRASHES c
GROUP BY c.street_name
ORDER BY total_crashes DESC
LIMIT 10;
```
![Calles con más accidentes](figures/calles.png)

3. Proporción de accidentes por condición de iluminación

```sql
SELECT
    cc.lighting_condition,
    COUNT(*) AS total_crashes,
    COUNT(*) * 1.0 / SUM(COUNT(*)) OVER () AS crash_share
FROM crash_circumstances cc
WHERE cc.lighting_condition IS NOT NULL
GROUP BY cc.lighting_condition
ORDER BY crash_share DESC;
```
Donde crash_share representa la proporción de accidentes asociada a cada condición de iluminación respecto al total.
![Condición de iluminación](figures/iluminacion.png)

### II. Condiciones de clima y fecha
4. Condiciones climáticas asociadas a más accidentes

```sql
SELECT 
    cc.weather_condition,
    COUNT(*) AS total_crashes
FROM CRASHES c
JOIN CRASH_CIRCUMSTANCES cc
    ON c.crash_record_id = cc.crash_record_id
GROUP BY cc.weather_condition
ORDER BY total_crashes DESC;
```
![Accidentes por clima](figures/clima_choques.png)

5. Severidad de lesiones por condición climática
   
```sql
SELECT
    cc.weather_condition,
    SUM(ci.injuries_fatal) AS fatalities,
    SUM(ci.injuries_incapacitating) AS severe_injuries
FROM CRASHES c
JOIN CRASH_CIRCUMSTANCES cc
    ON c.crash_record_id = cc.crash_record_id
JOIN CRASH_INJURIES ci
    ON c.crash_record_id = ci.crash_record_id
GROUP BY cc.weather_condition
ORDER BY fatalities DESC;
```

6. Accidentes por día de la semana y mes 

```sql
SELECT
    cd.crash_day_of_week,
    cd.crash_month,
    COUNT(*) AS total_crashes
FROM CRASH_DATE cd
GROUP BY cd.crash_day_of_week, cd.crash_month
ORDER BY total_crashes DESC;
```

7. Horario con más accidentes y lesiones
   
```sql
SELECT
    CASE
      WHEN EXTRACT(HOUR FROM c.incident_date) BETWEEN 0 AND 5  THEN 'Madrugada (0-5)'
      WHEN EXTRACT(HOUR FROM c.incident_date) BETWEEN 6 AND 11 THEN 'Mañana (6-11)'
      WHEN EXTRACT(HOUR FROM c.incident_date) BETWEEN 12 AND 17 THEN 'Tarde (12-17)'
      ELSE 'Noche (18-23)'
    END AS time_band,
    COUNT(*) AS total_crashes,
    SUM(ci.injuries_fatal
        + ci.injuries_incapacitating
        + ci.injuries_other) AS total_injuries
FROM crashes c
JOIN crash_injuries ci
  ON c.crash_record_id = ci.crash_record_id
GROUP BY time_band
ORDER BY total_injuries DESC;
```

### III. Condiciones del conductor
8. Accidentes con alcohol involucrado y severidad del choque

```sql
SELECT
    COUNT(DISTINCT di.person_id) AS drivers_with_alcohol,
    SUM(ci.injuries_fatal) AS fatalities,
    SUM(ci.injuries_incapacitating) AS severe_injuries,
    SUM(ci.injuries_other) AS minor_injuries
FROM driver_info di
JOIN people p
    ON di.person_id = p.person_id
JOIN crash_injuries ci
    ON p.crash_record_id = ci.crash_record_id
WHERE di.bac_result_value > 0;
```

9. Edad promedio de conductores en choques con y sin fallecidos

```sql
WITH fatal_flag AS (
	SELECT crash_record_id,
		   CASE WHEN injuries_fatal > 0 THEN 1 ELSE 0 END AS fatal_crash
	FROM crash_injuries
)
SELECT 
	CASE WHEN f.fatal_crash = 1 THEN 'CHOQUE CON FALLECIDOS'
		ELSE 'CHOQUE SIN FALLECIDOS' END AS tipo_choque,
	AVG(p.age) AS avg_driver_age,
	COUNT(*) AS total_drivers
FROM people p
JOIN fatal_flag f USING (crash_record_id)
WHERE p.person_type = 'DRIVER'
GROUP BY f.fatal_crash
ORDER BY avg_driver_age;
```
![Edad de conductores](figures/edad.png)

10. Uso de teléfono vs consumo de alcohol

```sql
WITH drivers_alcohol AS (
    SELECT DISTINCT c.crash_record_id
    FROM crashes c
    JOIN people p
        ON c.crash_record_id = p.crash_record_id
    JOIN driver_info di
        ON p.person_id = di.person_id
    WHERE p.person_type = 'DRIVER'
      AND (
            di.bac_result_value > 0
         OR di.physical_condition = 'IMPAIRED - ALCOHOL'
         OR di.physical_condition = 'HAD BEEN DRINKING'
         OR di.physical_condition = 'IMPAIRED - ALCOHOL AND DRUGS'
      )
),
drivers_phone AS (
    SELECT DISTINCT c.crash_record_id
    FROM crashes c
    JOIN people p
        ON c.crash_record_id = p.crash_record_id
    JOIN driver_info di
        ON p.person_id = di.person_id
    WHERE p.person_type = 'DRIVER'
      AND (
            di.cell_phone_use = TRUE
         OR di.driver_action = 'CELL PHONE USE OTHER THAN TEXTING'
         OR di.driver_action = 'TEXTING'
      )
)
SELECT
    (SELECT COUNT(*) FROM drivers_alcohol) AS alcohol_crashes,
    (SELECT COUNT(*) FROM drivers_phone)   AS phone_crashes;
```
![Casos de alcohol vs uso de celular](figures/alcoholvscel.png)

### IV. Condiciones del vehículo
11. Límite de velocidad

```sql
SELECT
    CASE
      WHEN cc.posted_speed_limit < 30 THEN '<30'
      WHEN cc.posted_speed_limit BETWEEN 30 AND 39 THEN '30–39'
      WHEN cc.posted_speed_limit BETWEEN 40 AND 49 THEN '40–49'
      WHEN cc.posted_speed_limit BETWEEN 50 AND 59 THEN '50–59'
      ELSE '60+'
    END AS speed_band,
    COUNT(*) AS total_crashes,
    SUM(ci.injuries_fatal
        + ci.injuries_incapacitating
        + ci.injuries_other)        AS total_injuries
FROM crash_circumstances cc
JOIN crash_injuries ci
  ON cc.crash_record_id = ci.crash_record_id
GROUP BY speed_band
ORDER BY speed_band DESC;
```

12. Choques por tipo de uso del vehículo

```sql
SELECT COALESCE(vs.vehicle_use, 'UNKNOWN') AS vehicle_use, COUNT(DISTINCT v.crash_record_id) AS total_crashes
FROM vehicle v
LEFT JOIN vehicle_specs vs 
ON v.vehicle_id= vs.vehicle_id
GROUP BY vehicle_use
ORDER BY total_crashes DESC;
```

13. Accidentes por marca y modelo

```sql
SELECT
    v.make,
    v.model,
    COUNT(DISTINCT v.crash_record_id) AS total_crashes
FROM vehicle v
WHERE v.make IS NOT NULL
  AND v.model IS NOT NULL
GROUP BY v.make, v.model
ORDER BY total_crashes DESC
LIMIT 10;
```
![Modelos de vehículo](figures/modelo.png)

### V. Hotspots
14. Identificación de hotspots

```sql
SELECT
    ROUND(latitude::numeric, 3)  AS lat_grid,
    ROUND(longitude::numeric, 3) AS lon_grid,
    COUNT(*) AS total_crashes
FROM crashes
WHERE latitude IS NOT NULL
  AND longitude IS NOT NULL
GROUP BY lat_grid, lon_grid
ORDER BY total_crashes DESC;
```
![Mapa de calor de accidentes](figures/mapacalor.png)

15.  Factores dominantes de cada hotspot

```sql
WITH grid AS (
    SELECT
        ROUND(crashes.latitude::numeric, 3)  AS lat_grid,
        ROUND(crashes.longitude::numeric, 3) AS lon_grid,
        crashes.crash_record_id
    FROM crashes crashes
    WHERE crashes.latitude IS NOT NULL
      AND crashes.longitude IS NOT NULL
)
SELECT
    grid.lat_grid,
    grid.lon_grid,
    COUNT(*) AS total_crashes,
    MODE() WITHIN GROUP (ORDER BY crash_circumstances.weather_condition) AS 					most_common_weather,
    MODE() WITHIN GROUP (ORDER BY crash_circumstances.lighting_condition)     AS most_common_lighting,
    MODE() WITHIN GROUP (ORDER BY crash_classification.crash_type)             AS most_common_crash_type
FROM grid 
JOIN crash_circumstances 
  ON grid.crash_record_id = crash_circumstances.crash_record_id
JOIN crash_classification 
  ON grid.crash_record_id = crash_classification.crash_record_id
GROUP BY grid.lat_grid, grid.lon_grid
HAVING COUNT(*) >= 30
ORDER BY total_crashes DESC
LIMIT 30;
```

