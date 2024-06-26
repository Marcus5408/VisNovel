import unittest
from visnovel import EmotionState, Character, Actor

class TestActorModule(unittest.TestCase):
    def setUp(self):
        self.valid_path = "tests/test.jpg"
        self.invalid_path = "/invalid/path/to/image"
        self.emotion1 = EmotionState("happy", self.valid_path)
        self.emotion2 = EmotionState("sad", self.valid_path)
        self.character = Character("John", [self.emotion1, self.emotion2], "happy")
        self.actor = Actor(self.character, "happy")

    def test_emotion_state(self):
        # test image path validation
        with self.assertRaises(FileNotFoundError):
            EmotionState("angry", "/invalid/path/to/image")

        # check object creation
        self.assertEqual(self.emotion1.emotion, "happy")
        # check image path assignment
        self.assertEqual(self.emotion1.image_path, self.valid_path)

    def test_character(self):
        # test duplicate emotion assignment error
        with self.assertRaises(KeyError):
            Character("John", [self.emotion1, self.emotion1], "happy")
        # test default emotion not found error
        with self.assertRaises(KeyError):
            Character("John", [self.emotion2], "happy")

        # check object creation
        self.assertEqual(self.character.name, "John")
        # check emotion assignment
        self.assertEqual(self.character.emotions, {"happy": self.valid_path, "sad": self.valid_path, "default": self.valid_path})

if __name__ == "__main__":
    unittest.main()