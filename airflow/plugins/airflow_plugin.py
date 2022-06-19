''' Da mesma forma como o PythonOperator, o operador que criamos, chamado TwitterOperator, também possui estas mesmas características, tornando-se genérico para qualquer interação que queiramos fazer com o Twitter, onde os parâmetros são chaves para especificar o tipo de requisição.
'''
from airflow.plugins_manager import AirflowPlugin
from operators.twitter_operator import TwitterOperator

class AluraAirflowPlugin(AirflowPlugin):
    name = "alura"
    operators = [TwitterOperator]
    