from abc import ABC, abstractmethod
import pickle

class DocVectorizerBase(ABC):
    @abstractmethod
    def fit(self, train_documents):
        pass

    @abstractmethod
    def fit_transform(self, train_documents):
        pass

    @abstractmethod
    def transform(self, documents):
        pass

    @abstractmethod
    def save(self, model_path):
        pass

    @classmethod
    def load(cls, model_path):
        vectorizer = pickle.load(open(model_path, "rb"))
        print(type(vectorizer))

        return vectorizer

