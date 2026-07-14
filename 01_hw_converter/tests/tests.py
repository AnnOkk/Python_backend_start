from unittest import TestCase,main
import pandas as pd
from converter import enumerator, columns_mapper, convert_x


class TestConvert(TestCase):

    def setUp(self):
        self.df = pd.DataFrame({
            "Company": [
                "Toyota",
                "Toyota",
                "Hundai",
                "Hundai",
                "Hundai"
            ],
            "Model": [
                "Camry",
                "Corolla",
                "i10",
                "Elantra",
                "Kona"
            ]
        })

    def test_enumerator(self):
        values = ["Toyota", "Hundai"]

        result = enumerator(values)

        expected = {
            "Toyota": 0,
            "Hundai": 1
        }

        self.assertEqual(result, expected)

    def test_enumerator_empty(self):
        result = enumerator([])

        self.assertEqual(result, {})

    def test_columns_mapper(self):
        result = columns_mapper(
            ["Company", "Model"],
            self.df
        )

        expected = {
            "Company": {
                "Toyota": 0,
                "Hundai": 1
            },
            "Model": {
                "Camry": 0,
                "Corolla": 1,
                "i10": 2,
                "Elantra": 3,
                "Kona": 4
            }
        }

        self.assertEqual(result, expected)

    def test_columns_mapper_one_column(self):
        result = columns_mapper(
            ["Company"],
            self.df
        )

        expected = {
            "Company": {
                "Toyota": 0,
                "Hundai": 1
            }
        }

        self.assertEqual(result, expected)

    def test_convert_x(self):
        mapper = {
            "Company": {
                "Toyota": 0,
                "Hundai": 1
            },
            "Model": {
                "Camry": 0,
                "Corolla": 1,
                "i10": 2,
                "Elantra": 3,
                "Kona": 4
            }
        }

        converted = convert_x(self.df, mapper)

        result = converted.to_dict(orient="list")

        expected = {
            "Company": [0, 0, 1, 1, 1],
            "Model": [0, 1, 2, 3, 4]
        }

        self.assertEqual(result, expected)

    def test_convert_x_with_generated_mapper(self):
        mapper = columns_mapper(
            ["Company", "Model"],
            self.df
        )

        converted = convert_x(self.df, mapper)

        expected = {
            "Company": [0, 0, 1, 1, 1],
            "Model": [0, 1, 2, 3, 4]
        }

        self.assertEqual(
            converted.to_dict(orient="list"),
            expected
        )

    def test_convert_x_does_not_change_original_dataframe(self):
        original = self.df.copy()

        mapper = columns_mapper(
            ["Company", "Model"],
            self.df
         )

        convert_x(self.df, mapper)

        self.assertTrue(self.df.equals(original))

if __name__ == "__main__":
    main()
