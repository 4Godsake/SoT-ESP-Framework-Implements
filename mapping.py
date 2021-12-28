"""
@Author https://github.com/DougTheDruid
@Source https://github.com/DougTheDruid/SoT-ESP-Framework
"""

ships = {
    # ------------ SHIPS / AI SHIPS ------------
    "BP_SmallShipTemplate_C": {
        "Name": "单帆",
    },
    "BP_SmallShipNetProxy_C": {
        "Name": "单帆*",
    },

    "BP_MediumShipTemplate_C": {
        "Name": "双帆",
    },
    "BP_MediumShipNetProxy_C": {
        "Name": "双帆*",
    },

    "BP_LargeShipTemplate_C": {
        "Name": "三帆",
    },
    "BP_LargeShipNetProxy_C": {
        "Name": "三帆*",
    },

    "BP_AISmallShipTemplate_C": {
        "Name": "小骷髅船",
    },
    "BP_AISmallShipNetProxy_C": {
        "Name": "小骷髅船*",
    },
    "BP_AILargeShipTemplate_C": {
        "Name": "大骷髅船",
    },
    "BP_AILargeShipNetProxy_C": {
        "Name": "大骷髅船*",
    },
    "BP_TinySharkExperience_C": {
        "Name": "鲨鱼地区",
    },
    "BP_TinyShark_C": {
        "Name": "鲨鱼",
    },
    "BP_Storm_C": {
        "Name": "风暴",
    },
    "BP_LegendSkellyFort_SkullCloud_C": {
        "Name": "红骷髅",
    },
    "BP_SkellyFort_SkullCloud_C": {
        "Name": "骷髅岛",
    },
    "BP_GhostShips_Signal_Flameheart_NetProxy_C": {
        "Name": "小红",
    },
    "BP_AshenLord_SkullCloud_C": {
        "Name": "火龙卷",
    },
    "BP_FogBank_C": {
        "Name": "白雾",
    },
    "BP_SkellyShip_ShipCloud_C": {
        "Name": "船云",
    },
    # "BP_AggressiveGhostShip_C": {
    #     "Name": "Flameheart Galleon",
    # },  # To implement, must modify ship.py's update method for visibility
}
players = {
    # ------------ player & NPC ------------
    "BP_PlayerPirate_C": {
        "Name": "player",
    },
    "BP_SkeletonPawnBase_C": {
        "Name": "npc",
    },
    "BP_SirenGruntPawn_C": {
        "Name": "siren",
    },
    "BP_Mermaid_C": {
        "Name": "美人鱼",
    },
    # "BP_CollectorsChest_Proxy_C": {
    #     "Name": "chest",
    # },
    # "BP_SK_CoralChest_Proxy_Legendary_C": {
    #     "Name": "chest",
    # },
    # "BP_SK_CoralCollectorsChest_Proxy_C": {
    #     "Name": "chest",
    # },
    # "BP_MerchantCrate_GunpowderBarrel_ItemInfo_C": {
    #     "Name": "火药",
    # },
    "BP_Shark_C": {
        "Name": "鲨鱼",
    },
    # "BP_AmmoPouchProxy_C": {
    #     "Name": "子弹",
    # },

}
cannons = {
    # ------------ cannons ------------
    "BP_Projectile_CannonBall_C": {
        "Name": "!",
    },
    "BP_Projectile_CannonBall_ChainShot_C": {
        "Name": "!",
    },
    "BP_Projectile_Grenade_Scatter_C": {
        "Name": "!",
    },
    "BP_Projectile_CannonBall_Cur_Fire_C": {
        "Name": "!",
    },
    # "BP_TaleBook_Shroudbreaker_SanctuaryOutpost_AdditionalPuzzles_C": {
    #     "Name": "BP_TaleBook_Shroudbreaker_SanctuaryOutpost_AdditionalPuzzles_C",
    # },


}

ship_keys = set(ships.keys())
player_keys = set(players.keys())
cannon_keys = set(cannons.keys())
