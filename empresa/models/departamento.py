from dataclasses import dataclass, asdict
from datetime import datetime, date
from typing import Optional

@dataclass
class Departamento:

    _numero: int
    _nome: str
    _cpf_gerente: Optional[str] = None
    _data_ini: Optional[date] = None
    _created_at: Optional[datetime] = None
    _updated_at: Optional[datetime] = None

    # Departamento -> dict
    def to_dict(self) -> dict:
        def _to_iso(v):
            if isinstance(v, (datetime, date)):
                return v.isoformat()
            return v

        return {
            'numero': self._numero,
            'nome': self._nome,
            'cpf_gerente': self._cpf_gerente,
            'data_ini': _to_iso(self._data_ini) if self._data_ini else None,
            'created_at': _to_iso(self._created_at) if self._created_at else None,
            'updated_at': _to_iso(self._updated_at) if self._updated_at else None,
        }

    # dict -> Departamento
    @classmethod
    def from_dict(cls, data: dict) -> 'Departamento':
        dn = data.get('data_ini')
        if isinstance(dn, str):
            try:
                if 'T' in dn:
                    dn = datetime.fromisoformat(dn)
                else:
                    dn = date.fromisoformat(dn)
            except Exception:
                pass

        ca = data.get('created_at')
        if isinstance(ca, str):
            try:
                ca = datetime.fromisoformat(ca)
            except Exception:
                ca = None

        ua = data.get('updated_at')
        if isinstance(ua, str):
            try:
                ua = datetime.fromisoformat(ua)
            except Exception:
                ua = None

        return Departamento(
            data.get('numero'),
            data.get('nome'),
            data.get('cpf_gerente'),
            dn,
            ca,
            ua
        )

    def __str__(self) -> str:
        return (
            f'Departamento(numero={self._numero}, nome={self._nome}, '
            f'cpf_gerente={self._cpf_gerente}, data_ini={self._data_ini}, '
            f'created_at={self._created_at}, updated_at={self._updated_at})'
        )

    # --- Properties ---
    @property
    def numero(self) -> int:
        return self._numero

    @numero.setter
    def numero(self, numero: int):
        self._numero = numero
        self._updated_at = datetime.now()

    @property
    def nome(self) -> str:
        return self._nome

    @nome.setter
    def nome(self, nome: str):
        self._nome = nome
        self._updated_at = datetime.now()

    @property
    def cpf_gerente(self) -> Optional[str]:
        return self._cpf_gerente

    @cpf_gerente.setter
    def cpf_gerente(self, cpf_gerente: Optional[str]):
        self._cpf_gerente = cpf_gerente
        self._updated_at = datetime.now()

    @property
    def data_ini(self) -> Optional[date]:
        return self._data_ini

    @data_ini.setter
    def data_ini(self, data_ini: Optional[date]):
        self._data_ini = data_ini
        self._updated_at = datetime.now()

    @property
    def created_at(self) -> Optional[datetime]:
        return self._created_at

    @property
    def updated_at(self) -> Optional[datetime]:
        return self._updated_at
