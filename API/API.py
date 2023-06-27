class API:
    @classmethod
    def devolver(cls,frase:str)->str:
        frase={
            'clave':frase
        }
        contenido=frase['clave']
        return contenido.upper()