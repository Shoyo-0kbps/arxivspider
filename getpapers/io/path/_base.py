import abc
import json
import typing
from pathlib import Path

from io.configs import LOCAL_PATH

class PathHandler(abc.ABC):
    
    _path : str

    def __init__(self, dir_name : str, make_dir : bool) -> None:
        """

        """
        self._path = dir_name

        if make_dir:
            self.mk_dir()

    @abc.abstractmethod
    def mk_dir(self) -> None:
        """

        """
        raise NotImplementedError("not implemented yet")


    
    @abc.abstractclassmethod
    def ls_dir(self) -> typing.List[str]:
        """
        
        """
        raise NotImplementedError("not implemented yet")
    
    @abc.abstractmethod
    def is_a_dir(self, dir_name : str) -> bool:
        """

        """
        raise NotImplementedError("not implemented yet")

    @abc.abstractclassmethod
    def _del_dir(self, del_dir : bool = False) -> None:
        """

        """
        raise NotImplementedError("not implemented yet")

    @abc.abstractclassmethod
    def _rnm_dir(self, src_name : str, dest_name : str):
        """

        """
        raise NotImplementedError("not implemented yet")

    @abc.abstractclassmethod
    def _del_content(self, del_content : str) -> None:
        """

        """
        raise NotImplementedError("not implemented yet")

    def del_dir(self, del_dir : bool = False) -> None:
        """
        
        """
        if len(self.ls_dir()) > 0 and not del_dir:
           raise PermissionError("Directory os not empty")
        else:
            self._del_dir(del_dir)

    def rename_dir(self, src_name : str, dest_name : str) -> None:
        """

        """
        if src_name not in self.ls_dir():
            raise FileNotFoundError(f" Directory {src_name} not found in {self._path}")
        else:
            self._rnm_dir(src_name, dest_name)
    
    def del_content(self, content_name : str) -> None:
        """

        """
        if content_name not in self.ls_dir():
            raise FileNotFoundError(f"{content_name} not found in {self._path}")
        else:
            self._del_content(content_name)
