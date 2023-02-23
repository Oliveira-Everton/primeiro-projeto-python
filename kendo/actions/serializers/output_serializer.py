from ..managers.revolver_manager import RevolverManager
from ..managers.hat_manager import HatManager
from ..constants.object_names import ObjectNames
from ..constants.operation_names import OperationNames


class OutputSerializer:

    _NO_ITEM = {
        ObjectNames.REVOLVER: 'Nem tenho revólver uai',
        ObjectNames.HAT: 'Nem tenho chapéu uai'
    }

    _ACTIONES = {
        OperationNames.GETTING: {
            ObjectNames.REVOLVER:{
                RevolverManager.GOTTEN_FROM_BAG: 'Peguei o revólver',
                RevolverManager.HOLDING_REVOLVER: 'Já tá na mão uai',
                RevolverManager.NO_REVOLVER: _NO_ITEM['revolver']
            },
            ObjectNames.HAT:{
                HatManager.GOTTEN_FROM_BAG: 'Botei o chapéu',
                HatManager.WEARING_HAT:  'Já estou com ele',
                HatManager.NO_HAT: _NO_ITEM['hat'] 
            }
        },

        OperationNames.PUTTING: {
            ObjectNames.REVOLVER:{
                RevolverManager.PUT_IN_BAG: 'Guardei o revólver',
                RevolverManager.REVOLVER_IN_BAG: 'Já está guardado uai',
                RevolverManager.NO_REVOLVER: _NO_ITEM['revolver']
            },
            ObjectNames.HAT:{
                HatManager.PUT_IN_BAG: 'Guardei o chapéu',
                HatManager.HAT_IN_BAG: 'Já está guardado',
                HatManager.NO_HAT: _NO_ITEM['hat']
            }
        }
    }

    def output_string(self, action, item, command):
        return self._ACTIONES[action][item][command]
