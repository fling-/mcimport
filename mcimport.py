import os
import sys
from block import *
import content

mcmap = MCMap(sys.argv[1])
mtmap = MTMap(sys.argv[2])

if not os.path.exists(sys.argv[2]):
    os.makedirs(sys.argv[2])

if not os.path.exists(sys.argv[2] + "/map_meta.txt"):
    mg = open(sys.argv[2] + "/map_meta.txt", "w")
    mg.write("mg_name = singlenode\n")
    mg.write("mapgen_singlenode = \"ignore\"\n")
    mg.write("waterlevel = 63\n")
    mg.write("[end_of_params]\n")
    mg.close()

if not os.path.exists(sys.argv[2] + "/world.mt"):
    wo = open(sys.argv[2] + "/world.mt", "w")
    wo.write("backend = sqlite3\n")
    wo.write("gameid = minetest\n")
    wo.write("load_mod_biome_lib = true\n")
    wo.write("load_mod_bushes_classic = true\n")
    wo.write("load_mod_crafting = true\n")
    wo.write("load_mod_ferns = true\n")
    wo.write("load_mod_flowers_plus = true\n")
    wo.write("load_mod_homedecor = true\n")
    wo.write("load_mod_junglegrass = true\n")
    wo.write("load_mod_lapis = true\n")
    wo.write("load_mod_mesecons = true\n")
    wo.write("load_mod_mesecons_button = true\n")
    wo.write("load_mod_mesecons_commandblock = true\n")
    wo.write("load_mod_mesecons_delayer = true\n")
    wo.write("load_mod_mesecons_doors = true\n")
    wo.write("load_mod_mesecons_lamp = true\n")
    wo.write("load_mod_mesecons_lightstone = true\n")
    wo.write("load_mod_mesecons_materials = true\n")
    wo.write("load_mod_mesecons_mvps = true\n")
    wo.write("load_mod_mesecons_noteblock = true\n")
    wo.write("load_mod_mesecons_pistons = true\n")
    wo.write("load_mod_mesecons_pressureplates = true\n")
    wo.write("load_mod_mesecons_receiver = true\n")
    wo.write("load_mod_mesecons_solarpanel = true\n")
    wo.write("load_mod_mesecons_switch = true\n")
    wo.write("load_mod_mesecons_torch = true\n")
    wo.write("load_mod_mesecons_walllever = true\n")
    wo.write("load_mod_moreblocks = true\n")
    wo.write("load_mod_moretrees = true\n")
    wo.write("load_mod_nether = true\n")
    wo.write("load_mod_poisonivy = true\n")
    wo.write("load_mod_quartz = true\n")
    wo.write("load_mod_vines = true\n")
    wo.write("load_mod_signs = true\n")
    wo.write("load_mod_signs_lib = true\n")
    wo.close()

#os.makedirs(sys.argv[2]+"/worldmods")
#os.makedirs(sys.argv[2]+"/worldmods/singlenode")

#sn = open(sys.argv[2]+"/worldmods/singlenode/init.lua", "w")
#sn.write("minetest.set_mapgen_params({mgname = \"singlenode\"})\n")
#sn.close()

if not os.path.exists(sys.argv[2]+"/moretrees_settings.txt"):
    mo = open(sys.argv[2]+"/moretrees_settings.txt", "w")
    mo.write("moretrees.enable_apple_tree = false\n")
    mo.write("moretrees.enable_oak = false\n")
    mo.write("moretrees.enable_sequoia = false\n")
    mo.write("moretrees.enable_palm = false\n")
    mo.write("moretrees.enable_pine = false\n")
    mo.write("moretrees.enable_rubber_tree = false\n")
    mo.write("moretrees.enable_willow = false\n")
    mo.write("moretrees.enable_acacia = false\n")
    mo.write("moretrees.enable_birch = false\n")
    mo.write("moretrees.enable_spruce = false\n")
    mo.write("moretrees.enable_jungle_tree = false\n")
    mo.write("moretrees.enable_fir = false\n")
    mo.write("moretrees.enable_beech = false\n")
    mo.close()

nimap, ct = content.read_content(["MORETREES", "NETHER", "QUARTZ"])
mtmap.fromMCMap(mcmap, nimap, ct)
mtmap.save()

