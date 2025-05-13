import streamlit as st
import tensorflow as tf
"""
[     UTC     ] Logs for sumar-numeros.streamlit.app/

────────────────────────────────────────────────────────────────────────────────────────

[01:40:38] 🖥 Provisioning machine...

[01:40:38] 🎛 Preparing system...

[01:40:38] ⛓ Spinning up manager process...

[01:40:35] 🚀 Starting up repository: 'sumar-numeros', branch: 'main', main module: 'app.py'

[01:40:35] 🐙 Cloning repository...

[01:40:35] 🐙 Cloning into '/mount/src/sumar-numeros'...

[01:40:35] 🐙 Cloned repository!

[01:40:35] 🐙 Pulling code changes from Github...

[01:40:35] 📦 Processing dependencies...


──────────────────────────────────────── uv ───────────────────────────────────────────


Using uv pip install.

Using Python 3.12.10 environment at /home/adminuser/venv

Resolved 63 packages in 694ms

Prepared 63 packages in 15.53s

Installed [2025-05-13 01:40:53.607459] 63 packages[2025-05-13 01:40:53.607758]  [2025-05-13 01:40:53.608796] in 1.02s[2025-05-13 01:40:53.609267] 

 + absl-py==2.2.2

 + altair==5.5.0

 + astunparse==1.6.3

 [2025-05-13 01:40:53.610085] + attrs==25.3.0

 + blinker==1.9.0

 + cachetools==5.5.2

 + certifi==2025.4.26[2025-05-13 01:40:53.610335] 

 + charset-normalizer==3.4.2

 + click==8.2.0

 + flatbuffers==[2025-05-13 01:40:53.610530] 25.2.10

 + gast==0.6.0

 + gitdb==4.0.12

 + gitpython[2025-05-13 01:40:53.610839] ==3.1.44

 + google-pasta==0.2.0

 + grpcio==1.71.0

 +[2025-05-13 01:40:53.611094]  h5py==3.13.0

 + idna==3.10

 + jinja2==3.1.6[2025-05-13 01:40:53.611455] 

 + jsonschema==4.23.0

 + jsonschema-specifications==2025.4.1

 + keras==3.9.2[2025-05-13 01:40:53.612165] 

 + libclang==18.1.1

 + markdown==3.8

 + markdown-it-py[2025-05-13 01:40:53.612487] ==3.0.0

 + markupsafe==3.0.2

 + mdurl==0.1.2[2025-05-13 01:40:53.612807] 

 + ml-dtypes==0.5.1

 + namex==0.0.9

 + narwhals==1.39.0[2025-05-13 01:40:53.613115] 

 + numpy==2.1.3

 + opt-einsum==3.4.0

 + optree==0.15.0

 + packaging==24.2

 + pandas==2.2.3

 + pillow==11.2.1

 + protobuf==5.29.4

 + pyarrow==20.0.0

 + pydeck==0.9.1

 + pygments==2.19.1

 + python-dateutil==2.9.0.post0

 + pytz==[2025-05-13 01:40:53.613323] 2025.2

 + referencing==0.36.2

 + requests==2.32.3

 + rich==14.0.0

 + rpds-py==0.24.0

 + setuptools==80.4.0

 + six==1.17.0

 + smmap==5.0.2

 +[2025-05-13 01:40:53.613536]  streamlit==1.45.1

 + tenacity==9.1.2

 + tensorboard==2.19.0

 + tensorboard-data-server==0.7.2

 + tensorflow==2.19.0

 + termcolor==3.1.0

 + toml==0.10.2

 + tornado==6.4.2

 + typing-extensions==4.13.2

 + tzdata==2025.2

 + urllib3==2.4.0

 + watchdog==6.0.0

 + werkzeug==3.1.3

 [2025-05-13 01:40:53.613785] + wheel==0.45.1

 + wrapt==1.17.2

Checking if Streamlit is installed

Found Streamlit version 1.45.1 in the environment

Installing rich for an improved exception logging

Using uv pip install.

Using Python 3.12.10 environment at /home/adminuser/venv

Audited 1 package in 3ms


────────────────────────────────────────────────────────────────────────────────────────


[01:40:55] 🐍 Python dependencies were installed from /mount/src/sumar-numeros/requirements.txt using uv.

Check if streamlit is installed

Streamlit is already installed

[01:40:56] 📦 Processed dependencies!




2025-05-13 01:41:09.728171: I external/local_xla/xla/tsl/cuda/cudart_stub.cc:32] Could not find cuda drivers on your machine, GPU will not be used.

2025-05-13 01:41:09.734395: I external/local_xla/xla/tsl/cuda/cudart_stub.cc:32] Could not find cuda drivers on your machine, GPU will not be used.

2025-05-13 01:41:09.755944: E external/local_xla/xla/stream_executor/cuda/cuda_fft.cc:467] Unable to register cuFFT factory: Attempting to register factory for plugin cuFFT when one has already been registered

WARNING: All log messages before absl::InitializeLog() is called are written to STDERR

E0000 00:00:1747100469.793756     202 cuda_dnn.cc:8579] Unable to register cuDNN factory: Attempting to register factory for plugin cuDNN when one has already been registered

E0000 00:00:1747100469.805443     202 cuda_blas.cc:1407] Unable to register cuBLAS factory: Attempting to register factory for plugin cuBLAS when one has already been registered

W0000 00:00:1747100469.837350     202 computation_placer.cc:177] computation placer already registered. Please check linkage and avoid linking the same target more than once.

W0000 00:00:1747100469.837405     202 computation_placer.cc:177] computation placer already registered. Please check linkage and avoid linking the same target more than once.

W0000 00:00:1747100469.837410     202 computation_placer.cc:177] computation placer already registered. Please check linkage and avoid linking the same target more than once.

W0000 00:00:1747100469.837413     202 computation_placer.cc:177] computation placer already registered. Please check linkage and avoid linking the same target more than once.

2025-05-13 01:41:09.847122: I tensorflow/core/platform/cpu_feature_guard.cc:210] This TensorFlow binary is optimized to use available CPU instructions in performance-critical operations.

To enable the following instructions: AVX2 FMA, in other operations, rebuild TensorFlow with the appropriate compiler flags.
"""

def sumar_enteros(a, b):
  """Suma dos números enteros utilizando TensorFlow.

  Args:
    a: El primer número entero (TensorFlow Tensor o Python integer).
    b: El segundo número entero (TensorFlow Tensor o Python integer).

  Returns:
    Un TensorFlow Tensor que contiene la suma de a y b.
  """
  a_tensor = tf.constant(a, dtype=tf.int32)
  b_tensor = tf.constant(b, dtype=tf.int32)
  suma = tf.add(a_tensor, b_tensor)
  return suma

st.title("Sumador de Enteros con TensorFlow")

numero1 = st.number_input("Ingrese el primer número entero", step=1, format="%d")
numero2 = st.number_input("Ingrese el segundo número entero", step=1, format="%d")

if st.button("Sumar"):
  if isinstance(numero1, (int, float)) and numero1 == int(numero1) and \
     isinstance(numero2, (int, float)) and numero2 == int(numero2):
    resultado_tensor = sumar_enteros(int(numero1), int(numero2))
    resultado = resultado_tensor.numpy()
    st.success(f"La suma de {int(numero1)} y {int(numero2)} es: {resultado}")
  else:
    st.error("Por favor, ingrese números enteros válidos.")
