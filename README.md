# Experimento HCI – Detección de IA vs Persona (Tarea de Negociación)

## Configuración de ambiente

### Requisitos
- Python 3.10

### Instalación
1. Clona el repositorio:
   ```bash
   git clone <URL_DEL_REPOSITORIO>
   cd tp-exp-ia-vs-personas
   ```

2. Crea un entorno virtual:
   ```bash
   python3.10 -m venv .venv
   ```

3. Activa el entorno virtual:
   - En macOS/Linux:
     ```bash
     source .venv/bin/activate
     ```
   - En Windows:
     ```bash
     .venv\Scripts\activate
     ```

4. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

### Como ejecutar
Para ejecutar el proyecto, utiliza el siguiente comando:
```bash
python main.py
```

## Objetivo General
Este experimento busca determinar si las personas son capaces de identificar correctamente si su contraparte en una interacción de negociación breve es un ser humano o una inteligencia artificial. Además, pretende explorar qué factores como el estilo de respuesta, la velocidad de contestación o la forma de argumentar influyen en dicha capacidad de detección. Permitirá profundizar en la interacción de qué tan perceptible es la interacción con modelos agenticos en situaciones cotidianas o comunes.

## Hipótesis
### Proporción de aciertos
- **H0 (nula):** La proporción de aciertos en la identificación de la contraparte es igual entre el grupo Persona–Persona y el grupo Persona–IA. 
  - PA_PP = PA_PIA
- **H1 (alternativa):** La proporción de aciertos en la identificación de la contraparte difiere entre el grupo Persona–Persona y el grupo Persona–IA.
  - PA_PP ≠ PA_PIA

### Tiempo de respuesta
- **H0 (nula):** El tiempo medio de respuesta para identificar la contraparte es igual entre el grupo Persona–Persona y el grupo Persona–IA.
  - TR_PP = TR_PIA
- **H1 (alternativa):** El tiempo medio de respuesta para identificar la contraparte difiere entre el grupo Persona–Persona y el grupo Persona–IA.
  - TR_PP ≠ TR_PIA

## Variables
### Independientes
- **Tipo de contraparte:** Humana o IA.

### Control
- **Latencia de respuesta:** Se usará un tiempo de respuesta de al menos 15 segundos para ocultar mejor el hecho de que un modelo responda rápido y permita al sujeto identificarlo con mayor facilidad.
- **Estilo de negociación:** Se configurará al modelo, a través del prompt, una personalidad balanceada.
- **Introducción de errores:** Se utilizará un prompt al modelo para que no dé respuestas 100% correctas y simular fallo humano.

### Modelo Utilizado
- Se utilizará un modelo de OpenAI GPT 4.1 en todas las interacciones.

### Dependientes
- **Acierto en la identificación:** Posibles valores son SI o NO. Se medirá consultando al sujeto si cree que la contraparte es o no una IA.
- **Tiempo para tomar la decisión:** Medido en milisegundos desde que la pregunta se muestra hasta que el sujeto responde.

### Confusoras
- **Edad de los participantes:** Se solicitará al sujeto que ingrese su edad.
- **Familiaridad con el uso de IA:** Medida con una escala de Likert de 5 puntos.
- **Alfabetización digital:** Medida con una escala de Likert de 5 puntos.
- **Educación:** Medida con una escala de Likert de 5 puntos.

## Participantes
Los participantes serán adultos mayores de 18 años de población universitaria y general, con un mínimo de 120 participantes. Se informará sobre la finalidad, el tiempo estimado, la privacidad y el uso de decepción parcial, aclarada en el debriefing final. Se solicitarán datos de edad, formación, familiaridad con IA, nivel de alfabetización digital e idioma nativo. Preferentemente se seleccionarán sujetos que hablen español.

## Formación de Grupos
- **G1:** Persona–Persona (P–P)
- **G2:** Persona–IA (P–IA)

Se seguirá un diseño inter-sujetos y la asignación será aleatoria.

## Tarea e Interacción
La tarea consiste en una negociación breve de entre dos y tres minutos, realizada de forma remota a través de la interfaz web. El participante y su contraparte deben repartirse tres objetos con valor distinto (por ejemplo, bicicleta, computadora y teléfono). La regla es que cada uno debe quedarse con al menos uno y llegar a un acuerdo. La contraparte puede ser un humano con guión o una IA con parámetros controlados. La tarea finaliza cuando se logra un acuerdo o se cumple el tiempo. Al terminar, el participante debe identificar si la contraparte era una persona o una IA, indicar su confianza, percepción de humanidad y justificar su respuesta.

## Ejecución en la Web
- **Asignación de condición y registro de interacción:** Gestionado por el back-end.
- **Control de latencias:** Instrucciones estandarizadas.
- **Medidas anti-bot.**

## Interfaz Web
La página web contará con:
- **Pantalla inicial:** Bienvenida, explicación general del estudio y acceso al consentimiento informado.
- **Pantalla de consentimiento informado:** Texto claro con detalles de participación, privacidad y botón para aceptar.
- **Cuestionario previo:** Formulario breve para datos demográficos y preguntas sobre familiaridad con IA.
- **Interfaz de chat:**
  - Panel principal con mensajes en formato burbuja.
  - Indicador visual de “escribiendo…” para simular latencia natural.
  - Cronómetro visible que muestre el tiempo restante.
  - Lista fija de objetos a negociar mostrada en un panel lateral o superior.
  - Campo de entrada de texto con botón “Enviar” y soporte para presionar Enter.
- **Pantalla post-tarea:** Cuestionario de identificación de contraparte y medición de tiempo de respuesta.
- **Pantalla de debriefing:** Explicación de la condición real y propósito del estudio, opción de retirar datos.
- **Redirección a Pantalla de análisis:** Para visualizar los datos globales del experimento.

## Sesgos y Validez
### Validez Interna
- **Instrucciones neutrales:** Redactadas para no sugerir que la contraparte pueda ser IA o persona.
- **Guiones estandarizados:** En P–P, los confederados seguirán un estilo de negociación definido.
- **Control de latencias:** Tiempos de respuesta similares en ambas condiciones.
- **Igual dificultad:** Misma lista de objetos y reglas en todas las sesiones.

### Validez Externa
- **Muestra diversa:** Incluir participantes de distintos perfiles.
- **Tareas realistas:** La negociación simula interacciones cotidianas.
- **Compatibilidad multiplataforma:** Experiencia consistente en distintos dispositivos y navegadores.

## Resultados

Para más detalles sobre los resultados del experimento, consulta el archivo [RESULTS.md](RESULTS.md).

## Datos

Para más detalles sobre los datos y sus visualizaciones, consulta el archivo [DATA.md](DATA.md).
