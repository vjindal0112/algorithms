from algorithms.is_unique_string import has_unique_chars


class TestIsUniqueString:
    def test_all_unique(self) -> None:
        assert has_unique_chars("asdfghjkl") is True

    def test_all_unique_2(self) -> None:
        assert has_unique_chars("wepto") is True

    def test_all_unique_3(self) -> None:
        assert has_unique_chars("qwertyuiopasdfghjklzxcvbnm") is True

    def test_non_unique(self) -> None:
        assert has_unique_chars("asdhjkla") is False

    def test_multi_non_unique(self) -> None:
        assert has_unique_chars("qwertyuioqwertyu") is False

    def test_multi_non_unique_2(self) -> None:
        assert has_unique_chars("thisisproblematic") is False
