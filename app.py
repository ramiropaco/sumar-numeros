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

# Ejemplo de uso
numero1 = 10
numero2 = 5
resultado_tensor = sumar_enteros(numero1, numero2)

# Para obtener el valor numérico del Tensor
resultado = resultado_tensor.numpy()
print(f"La suma de {numero1} y {numero2} es: {resultado}")

# También se puede trabajar directamente con Tensores
tensor_a = tf.constant(25, dtype=tf.int32)
tensor_b = tf.constant(12, dtype=tf.int32)
resultado_tensor_directo = tf.add(tensor_a, tensor_b)
resultado_directo = resultado_tensor_directo.numpy()
print(f"La suma de {tensor_a.numpy()} y {tensor_b.numpy()} es: {resultado_directo}")