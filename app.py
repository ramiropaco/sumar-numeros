import streamlit as st
import tensorflow as tf

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
