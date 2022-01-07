"""Dataclass for the Data Encoded into a Namecode Filename"""

from dataclasses import dataclass, field
from typing import Dict, Iterable, List, Literal, Optional, Tuple, Type, TypeVar, Union

from pydantic.fields import Field  # pylint: disable="no-name-in-module"
from pydantic.main import BaseModel

from nautilus_namecodes.scheme.v_0_1_0.filename import (
    Filename,
    NameCode,
)

# Decorate the Range Class with Pydantic.
# dataclass(NameCode)  # pylint: disable="c-extension-no-member"


class NautilusNamecodesFilenameBaseModel(BaseModel):
    """Pydantic Model for Nautilus Namecodes Filename"""

    encoding: Filename = Field(title="Filename")

    class Config:  # pylint: disable="missing-class-docstring"
        title = "Nautilus Namecodes Filename Dataclass"


if __name__ == "__main__":

    print(NautilusNamecodesFilenameBaseModel.schema_json())

    # nautilus_namecodes_model = NautilusNamecodesFilenameBaseModel()

    # print("\n\n\n\n\n\n")
    # print(nautilus_namecodes_model.schema_json(indent=2))
