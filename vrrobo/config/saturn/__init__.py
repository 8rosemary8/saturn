# Copyright (c) 2022-2024, The Isaac Lab Project Developers.
# All rights reserved.
#
# SPDX-License-Identifier: BSD-3-Clause

import gymnasium as gym

from . import agents

##
# Register Gym environments.
##

# gym.register(
#     id="saturn_gs",
#     entry_point="isaaclab.envs:ManagerBasedRLEnv",
#     disable_env_checker=True,
#     kwargs={
#         "env_cfg_entry_point": f"{__name__}.saturn_env_cfg.SaturnGSEnvCfg",
#         "rsl_rl_cfg_entry_point": f"{agents.__name__}.rsl_rl_ppo_cfg:UnitreeGo2GSPPORunnerCfg",
#     },
# )

# gym.register(
#     id="saturn_gs_play",
#     entry_point="isaaclab.envs:ManagerBasedRLEnv",
#     disable_env_checker=True,
#     kwargs={
#         "env_cfg_entry_point": f"{__name__}.saturn_env_cfg.UnitreeGo2GSEnvCfg_PLAY",
#         "rsl_rl_cfg_entry_point": f"{agents.__name__}.rsl_rl_ppo_cfg:UnitreeGo2GSPPORunnerCfg",
#     },
# )

gym.register(
    id="go2_gs",
    entry_point="isaaclab.envs:ManagerBasedRLEnv",
    disable_env_checker=True,
    kwargs={
        "env_cfg_entry_point": f"{__name__}.saturn_env_cfg.UnitreeGo2GSEnvCfg",
        "rsl_rl_cfg_entry_point": f"{agents.__name__}.rsl_rl_ppo_cfg:UnitreeGo2GSPPORunnerCfg",
    },
)

gym.register(
    id="go2_gs_play",
    entry_point="isaaclab.envs:ManagerBasedRLEnv",
    disable_env_checker=True,
    kwargs={
        "env_cfg_entry_point": f"{__name__}.saturn_env_cfg.UnitreeGo2GSEnvCfg_PLAY",
        "rsl_rl_cfg_entry_point": f"{agents.__name__}.rsl_rl_ppo_cfg:UnitreeGo2GSPPORunnerCfg",
    },
)
