from abc import ABC, abstractmethod

class RagService(ABC):
    @abstractmethod
    def ingest(self, data: str) -> None:
        pass