class CVResultMsg:
    def __init__(self, result: list) -> None:
        self.result = result

    def _get_art_score(self) -> float:
        artificial_result = list(filter(lambda x: x['label'] == 'artificial', self.result))[0]
        return round(artificial_result['score'], 2)

    def prettify(self) -> str:
        score = self._get_art_score()
        return f"Вероятность, что изображение сгенерировано: {score}"