def my_write_restart(step, t, t_wall, state):
    restart_data = {
        "volume_to_local_mesh_data": volume_to_local_mesh_data,
        "cv": state.cv,
        "av_smu": state.av_smu,
        "av_sbeta": state.av_sbeta,
        "av_skappa": state.av_skappa,
        "av_sd": state.av_sd,
        "temperature_seed": state.tseed,
        "nspecies": nspecies,
        "t": t,
        "step": step,
        "order": order,
        "last_viz_interval": last_viz_interval,
        "global_nelements": global_nelements,
        "num_parts": nparts
    }
    if use_wall:
        restart_data["wv"] = state.wv
        restart_data["t_wall"] = t_wall

    write_restart_file(actx, restart_data, restart_fname, comm)
