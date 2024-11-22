from os import path
import py_jwt_cpp

dummy_key_path = path.dirname(__file__)
dummy_key = open(path.join(path.dirname(__file__), 'dummy-key')).read()

def test__basic_encode():
    res = py_jwt_cpp.encode(
        data={'key': 'val'},
        private_key=dummy_key
    )

    expected_jwt = "eyJhbGciOiJSUzI1NiJ9.eyJrZXkiOiJ2YWwifQ.n3XngELQZfFD2QodamGMvyeDrT76lKDAxVW2Ihp3LWV65-MPShfS2f16dpaaXHr7K-Kf48XhSaC3Lo53httVyc56PZLBuGvghEhCnIT90YwRA-SnnBDlT80jygHTruZj-T-9Myt8kKlDuazjeqC7R54YGTk-BsEAJruNaY8_qp_ak4-GyfFh67CMRZ8h1Oa5nmoB_r0tpUr8TXgu-nDoerDqNEYN5VkGAZwpy9IhGL_2qigjHQ7S25VBgiz7YDOqEKnBs8yAeiOo1f0nidl7Ex-Z3NKeEv-bqdEY3KGe5aUvdIY7v5l16jioLTTClpJ3v87v9ao98xGst5OYSkHAAg"

    assert res == expected_jwt


def test__encode_with_headers():
    res = py_jwt_cpp.encode(
        data={'key': 'val'},
        private_key=dummy_key,
        headers={'kid': 'the-kid', 'typ': 'JWT'}
    )

    expected_jwt = 'eyJhbGciOiJSUzI1NiIsImtpZCI6InRoZS1raWQiLCJ0eXAiOiJKV1QifQ.eyJrZXkiOiJ2YWwifQ.nxJQBKWe2wzxoW_SH04D4eWefeN55tzf0l1HT_FMkdVJjjBhZ_f4VuHGHX_0BtZAnXj2HNMGaa4ZVy4Swz7HMk6gEolpyqgLfC3f1Yl10wo35TCsfGj-e-bQrg1pZmDska0NgLCkyKteIiU8l0Eos-QiBH63rUooDcTOP7mNW9rBOxisqeaZD3W8Ssm9fGFhUnKRVF1GpZZqabSW-hUKuwxPK_MwY0pYmB7RlhAEmjZV6TuFG-TYoNnxyAsLcW2hkLkOmD3eIuwp5fSuYpGfdcAReDjAi2O8YdP6UqmRg-1nPQ4ulx5vaKrjR4r5KbGHnVHgQHkJRo0vyZ4fnYHj5Q'

    assert res == expected_jwt
