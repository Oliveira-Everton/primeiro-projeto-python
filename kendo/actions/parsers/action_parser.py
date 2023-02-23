from ..constants.operation_names import OperationNames
from ..constants.object_names import ObjectNames
from ..serializers.output_serializer import OutputSerializer
from ..managers import RevolverManager, HatManager


class ActionParser:
    _ACTION = {
        OperationNames.GETTING:['get','pegar','equip', 'pegando'],
        OperationNames.PUTTING:['guardar', 'unequip', 'put'],
    }
    _ITEM = {
        ObjectNames.REVOLVER: ['arma', 'revólver', 'revolver', 'gun', 'weapon'],
        ObjectNames.HAT: ['hat', 'chapéu', 'chapeu']
            }

    def __init__(self, string_action, string_item, pessoa):
        self._string_action = string_action
        self._string_item = string_item
        self._pessoa = pessoa

    def _convert_action(self):
        for action, action_list in self._ACTION.items():
            if self._string_action in action_list:
                self._action = action

    def _convert_item(self):
        for item, item_list in self._ITEM.items():
            if self._string_item in item_list:
                self._item = item

    def _execute_action(self):
        if self._item == ObjectNames.REVOLVER:
            self._object_manager = RevolverManager(self._pessoa)
            return self._execute_action_revolver()
        else:
            self._object_manager = HatManager(self._pessoa)
            return self._execute_action_hat()

    def _execute_action_revolver(self):
        if self._action == OperationNames.GETTING:
            return self._object_manager.get_revolver()
        else:
            return self._object_manager.put_revolver()

    def _execute_action_hat(self):
        if self._action == OperationNames.GETTING:
            return self._object_manager.equip_hat()
        else:
            return self._object_manager.unequip_hat()

    def find_command(self):
        self._convert_action()
        self._convert_item()
        command = self._execute_action()
        return OutputSerializer().output_string(self._action, self._item, command)
