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
## Limpieza y Normalización de datos

## Análisis de datos a través de consultas SQL
Realizamos varias consultas de SQL para el análisis de la base de datos, descubriendo información valiosa para identificar y concluir acerca de factores de riesgo y patrones de accidentes 

### I. Condiciones Viales
### 1. Accidentes por defectos de la vía (road deffects)

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

### 2. Calles con más accidentes

```sql
SELECT
    c.street_name,
    COUNT(*) AS total_crashes
FROM CRASHES c
GROUP BY c.street_name
ORDER BY total_crashes DESC
LIMIT 10;

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
Donde crash_share representa la proporción de accidentes asociada a cada condición de iluminación respecto al total.



