import json

def limpar_entries(json_data):
    for objeto in json_data:
        if "entries" in objeto:
            entries = objeto["entries"]
            objeto["entries"] = [entry for entry in entries if not entry.startswith("Starting at")]
    
    return json_data

json_string = '''
{
	"_meta": {
		"internalCopies": [
			"race"
		]
	},
"subrace": [
		{
			"name": "Fallen",
			"source": "VGM",
			"raceName": "Aasimar",
			"raceSource": "VGM",
			"page": 105,
			"ability": [
				{
					"str": 1
				}
			],
			"entries": [
				{
					"name": "Necrotic Shroud",
					"entries": [
						"Starting at 3rd level, you can use your action to unleash the divine energy within yourself, causing your eyes to turn into pools of darkness and two skeletal, ghostly, flightless wings to sprout from your back. The instant you transform, other creatures within 10 feet of you that can see you must succeed on a Charisma saving throw (DC 8 + your proficiency bonus + your Charisma modifier) or become {@condition frightened} of you until the end of your next turn.",
						"Your transformation lasts for 1 minute or until you end it as a bonus action. During it, once on each of your turns, you can deal extra necrotic damage to one target when you deal damage to it with an attack or a spell. The extra necrotic damage equals your level.",
						"Once you use this trait, you can't use it again until you finish a long rest."
					],
					"type": "entries"
				}
			],
			"hasFluff": true,
			"hasFluffImages": true
		},
		{
			"name": "Protector",
			"source": "VGM",
			"raceName": "Aasimar",
			"raceSource": "VGM",
			"page": 105,
			"ability": [
				{
					"wis": 1
				}
			],
			"entries": [
				{
					"name": "Radiant Soul",
					"entries": [
						"Starting at 3rd level, you can use your action to unleash the divine energy within yourself, causing your eyes to glimmer and two luminous, incorporeal wings to sprout from your back.",
						"Your transformation lasts for 1 minute or until you end it as a bonus action. During it, you have a flying speed of 30 feet, and once on each of your turns, you can deal extra radiant damage to one target when you deal damage to it with an attack or a spell. The extra radiant damage equals your level.",
						"Once you use this trait, you can't use it again until you finish a long rest."
					],
					"type": "entries"
				}
			],
			"hasFluff": true,
			"hasFluffImages": true
		},
		{
			"name": "Scourge",
			"source": "VGM",
			"raceName": "Aasimar",
			"raceSource": "VGM",
			"page": 105,
			"ability": [
				{
					"con": 1
				}
			],
			"entries": [
				{
					"name": "Radiant Consumption",
					"entries": [
						"Starting at 3rd level, you can use your action to unleash the divine energy within yourself, causing a searing light to radiate from you, pour out of your eyes and mouth, and threaten to char you.",
						"Your transformation lasts for 1 minute or until you end it as a bonus action. During it, you shed bright light in a 10-foot radius and dim light for an additional 10 feet, and at the end of each of your turns, you and each creature within 10 feet of you take radiant damage equal to half your level (rounded up). In addition, once on each of your turns, you can deal extra radiant damage to one target when you deal damage to it with an attack or a spell. The extra radiant damage equals your level.",
						"Once you use this trait, you can't use it again until you finish a long rest."
					],
					"type": "entries"
				}
			],
			"hasFluff": true,
			"hasFluffImages": true
		},
		{
			"name": "Hawk-Headed",
			"source": "PSA",
			"raceName": "Aven",
			"raceSource": "PSA",
			"page": 16,
			"ability": [
				{
					"wis": 2
				}
			],
			"skillProficiencies": [
				{
					"perception": true
				}
			],
			"entries": [
				{
					"name": "Hawkeyed",
					"entries": [
						"You have proficiency in the {@skill Perception} skill. In addition, attacking at long range doesn't impose disadvantage on your ranged weapon attack rolls."
					],
					"type": "entries"
				}
			],
			"hasFluff": true,
			"hasFluffImages": true
		},
		{
			"name": "Ibis-Headed",
			"source": "PSA",
			"raceName": "Aven",
			"raceSource": "PSA",
			"page": 16,
			"ability": [
				{
					"int": 1
				}
			],
			"entries": [
				{
					"name": "Kefnet's Blessing",
					"entries": [
						"You can add half your proficiency bonus, rounded down, to any Intelligence check you make that doesn't already include your proficiency bonus."
					],
					"type": "entries"
				}
			],
			"hasFluff": true,
			"hasFluffImages": true
		},
		{
			"source": "PHB",
			"raceName": "Dragonborn",
			"raceSource": "PHB",
			"page": 32,
			"srd": true,
			"hasFluff": true,
			"hasFluffImages": true,
			"_versions": [
				{
					"_template": {
						"name": "Dragonborn ({{color}})",
						"source": "PHB",
						"_mod": {
							"entries": [
								{
									"mode": "removeArr",
									"names": "Draconic Ancestry"
								},
								{
									"mode": "replaceArr",
									"replace": "Breath Weapon",
									"items": {
										"type": "entries",
										"name": "Breath Weapon",
										"entries": [
											"You can use your action to exhale destructive energy in a {{area}}.",
											"When you use your breath weapon, each creature in the area of the exhalation must make a {{savingThrow}} saving throw. The DC for this saving throw equals 8 + your Constitution modifier + your proficiency bonus. A creature takes {@damage 2d6} {{damageType}} damage on a failed save, and half as much damage on a successful one. The damage increases to {@damage 3d6} at 6th level, {@damage 4d6} at 11th level, and {@damage 5d6} at 16th level.",
											"After you use your breath weapon, you can't use it again until you complete a short or long rest."
										]
									}
								},
								{
									"mode": "replaceArr",
									"replace": "Damage Resistance",
									"items": {
										"type": "entries",
										"name": "Damage Resistance",
										"entries": [
											"You have resistance to {{damageType}} damage."
										]
									}
								}
							]
						}
					},
					"_implementations": [
						{
							"_variables": {
								"color": "Black",
								"damageType": "acid",
								"area": "5-foot-wide, 30-foot-long line",
								"savingThrow": "Dexterity"
							},
							"resist": [
								"acid"
							]
						},
						{
							"_variables": {
								"color": "Blue",
								"damageType": "lightning",
								"area": "5-foot-wide, 30-foot-long line",
								"savingThrow": "Dexterity"
							},
							"resist": [
								"lightning"
							]
						},
						{
							"_variables": {
								"color": "Brass",
								"damageType": "fire",
								"area": "5-foot-wide, 30-foot-long line",
								"savingThrow": "Dexterity"
							},
							"resist": [
								"fire"
							]
						},
						{
							"_variables": {
								"color": "Bronze",
								"damageType": "lightning",
								"area": "5-foot-wide, 30-foot-long line",
								"savingThrow": "Dexterity"
							},
							"resist": [
								"lightning"
							]
						},
						{
							"_variables": {
								"color": "Copper",
								"damageType": "acid",
								"area": "5-foot-wide, 30-foot-long line",
								"savingThrow": "Dexterity"
							},
							"resist": [
								"acid"
							]
						},
						{
							"_variables": {
								"color": "Gold",
								"damageType": "fire",
								"area": "15-foot cone",
								"savingThrow": "Dexterity"
							},
							"resist": [
								"fire"
							]
						},
						{
							"_variables": {
								"color": "Green",
								"damageType": "poison",
								"area": "15-foot cone",
								"savingThrow": "Constitution"
							},
							"resist": [
								"poison"
							]
						},
						{
							"_variables": {
								"color": "Red",
								"damageType": "fire",
								"area": "15-foot cone",
								"savingThrow": "Dexterity"
							},
							"resist": [
								"fire"
							]
						},
						{
							"_variables": {
								"color": "Silver",
								"damageType": "cold",
								"area": "15-foot cone",
								"savingThrow": "Constitution"
							},
							"resist": [
								"cold"
							]
						},
						{
							"_variables": {
								"color": "White",
								"damageType": "cold",
								"area": "15-foot cone",
								"savingThrow": "Constitution"
							},
							"resist": [
								"cold"
							]
						}
					]
				}
			]
		},
		{
			"name": "Draconblood",
			"source": "EGW",
			"raceName": "Dragonborn",
			"raceSource": "PHB",
			"page": 168,
			"ability": [
				{
					"int": 2,
					"cha": 1
				}
			],
			"darkvision": 60,
			"resist": null,
			"entries": [
				{
					"type": "entries",
					"name": "Darkvision",
					"entries": [
						"You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. You can't discern color in darkness, only shades of gray."
					]
				},
				{
					"type": "entries",
					"name": "Forceful Presence",
					"entries": [
						"You can use your understanding of creative diplomacy or intimidation to guide a conversation in your favor. When you make a Charisma ({@skill Intimidation} or {@skill Persuasion}) check, you can do so with advantage. Once you use this trait, you can't do so again until you finish a short or long rest."
					],
					"data": {
						"overwrite": "Damage Resistance"
					}
				},
				{
					"name": "Draconic Ancestry",
					"entries": [
						"You have draconic ancestry. Choose one type of dragon from the Draconic Ancestry table. Your breath weapon is determined by the dragon type, as shown in the table.",
						{
							"type": "table",
							"caption": "Draconic Ancestry",
							"colLabels": [
								"Dragon",
								"Damage Type",
								"Breath Weapon"
							],
							"colStyles": [
								"col-3 text-center",
								"col-3 text-center",
								"col-6"
							],
							"rows": [
								[
									"Black",
									"Acid",
									"5 by 30 ft. line (Dex. save)"
								],
								[
									"Blue",
									"Lightning",
									"5 by 30 ft. line (Dex. save)"
								],
								[
									"Brass",
									"Fire",
									"5 by 30 ft. line (Dex. save)"
								],
								[
									"Bronze",
									"Lightning",
									"5 by 30 ft. line (Dex. save)"
								],
								[
									"Copper",
									"Acid",
									"5 by 30 ft. line (Dex. save)"
								],
								[
									"Gold",
									"Fire",
									"15 ft. cone (Dex. save)"
								],
								[
									"Green",
									"Poison",
									"15 ft. cone (Con. save)"
								],
								[
									"Red",
									"Fire",
									"15 ft. cone (Dex. save)"
								],
								[
									"Silver",
									"Cold",
									"15 ft. cone (Con. save)"
								],
								[
									"White",
									"Cold",
									"15 ft. cone (Con. save)"
								]
							]
						}
					],
					"type": "entries",
					"data": {
						"overwrite": "Draconic Ancestry"
					}
				}
			],
			"overwrite": {
				"ability": true,
				"traitTags": true
			},
			"hasFluff": true,
			"hasFluffImages": true,
			"_versions": [
				{
					"_template": {
						"name": "Dragonborn (Draconblood; {{color}})",
						"source": "EGW",
						"_mod": {
							"entries": [
								{
									"mode": "removeArr",
									"names": "Draconic Ancestry"
								},
								{
									"mode": "replaceArr",
									"replace": "Breath Weapon",
									"items": {
										"type": "entries",
										"name": "Breath Weapon",
										"entries": [
											"You can use your action to exhale destructive energy in a {{area}}.",
											"When you use your breath weapon, each creature in the area of the exhalation must make a {{savingThrow}} saving throw. The DC for this saving throw equals 8 + your Constitution modifier + your proficiency bonus. A creature takes {@damage 2d6} {{damageType}} damage on a failed save, and half as much damage on a successful one. The damage increases to {@damage 3d6} at 6th level, {@damage 4d6} at 11th level, and {@damage 5d6} at 16th level.",
											"After you use your breath weapon, you can't use it again until you complete a short or long rest."
										]
									}
								}
							]
						}
					},
					"_implementations": [
						{
							"_variables": {
								"color": "Black",
								"damageType": "acid",
								"area": "5-foot-wide, 30-foot-long line",
								"savingThrow": "Dexterity"
							}
						},
						{
							"_variables": {
								"color": "Blue",
								"damageType": "lightning",
								"area": "5-foot-wide, 30-foot-long line",
								"savingThrow": "Dexterity"
							}
						},
						{
							"_variables": {
								"color": "Brass",
								"damageType": "fire",
								"area": "5-foot-wide, 30-foot-long line",
								"savingThrow": "Dexterity"
							}
						},
						{
							"_variables": {
								"color": "Bronze",
								"damageType": "lightning",
								"area": "5-foot-wide, 30-foot-long line",
								"savingThrow": "Dexterity"
							}
						},
						{
							"_variables": {
								"color": "Copper",
								"damageType": "acid",
								"area": "5-foot-wide, 30-foot-long line",
								"savingThrow": "Dexterity"
							}
						},
						{
							"_variables": {
								"color": "Gold",
								"damageType": "fire",
								"area": "15-foot cone",
								"savingThrow": "Dexterity"
							}
						},
						{
							"_variables": {
								"color": "Green",
								"damageType": "poison",
								"area": "15-foot cone",
								"savingThrow": "Constitution"
							}
						},
						{
							"_variables": {
								"color": "Red",
								"damageType": "fire",
								"area": "15-foot cone",
								"savingThrow": "Dexterity"
							}
						},
						{
							"_variables": {
								"color": "Silver",
								"damageType": "cold",
								"area": "15-foot cone",
								"savingThrow": "Constitution"
							}
						},
						{
							"_variables": {
								"color": "White",
								"damageType": "cold",
								"area": "15-foot cone",
								"savingThrow": "Constitution"
							}
						}
					]
				}
			]
		},
		{
			"name": "Ravenite",
			"source": "EGW",
			"raceName": "Dragonborn",
			"raceSource": "PHB",
			"page": 168,
			"ability": [
				{
					"str": 2,
					"con": 1
				}
			],
			"darkvision": 60,
			"resist": null,
			"entries": [
				{
					"type": "entries",
					"name": "Darkvision",
					"entries": [
						"You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. You can't discern color in darkness, only shades of gray."
					]
				},
				{
					"type": "entries",
					"name": "Vengeful Assault",
					"entries": [
						"When you take damage from a creature in range of a weapon you are wielding, you can use your reaction to make an attack with the weapon against that creature. Once you use this trait, you can't do so again until you finish a short or long rest."
					],
					"data": {
						"overwrite": "Damage Resistance"
					}
				},
				{
					"name": "Draconic Ancestry",
					"entries": [
						"You have draconic ancestry. Choose one type of dragon from the Draconic Ancestry table. Your breath weapon is determined by the dragon type, as shown in the table.",
						{
							"type": "table",
							"caption": "Draconic Ancestry",
							"colLabels": [
								"Dragon",
								"Damage Type",
								"Breath Weapon"
							],
							"colStyles": [
								"col-3 text-center",
								"col-3 text-center",
								"col-6"
							],
							"rows": [
								[
									"Black",
									"Acid",
									"5 by 30 ft. line (Dex. save)"
								],
								[
									"Blue",
									"Lightning",
									"5 by 30 ft. line (Dex. save)"
								],
								[
									"Brass",
									"Fire",
									"5 by 30 ft. line (Dex. save)"
								],
								[
									"Bronze",
									"Lightning",
									"5 by 30 ft. line (Dex. save)"
								],
								[
									"Copper",
									"Acid",
									"5 by 30 ft. line (Dex. save)"
								],
								[
									"Gold",
									"Fire",
									"15 ft. cone (Dex. save)"
								],
								[
									"Green",
									"Poison",
									"15 ft. cone (Con. save)"
								],
								[
									"Red",
									"Fire",
									"15 ft. cone (Dex. save)"
								],
								[
									"Silver",
									"Cold",
									"15 ft. cone (Con. save)"
								],
								[
									"White",
									"Cold",
									"15 ft. cone (Con. save)"
								]
							]
						}
					],
					"type": "entries",
					"data": {
						"overwrite": "Draconic Ancestry"
					}
				}
			],
			"overwrite": {
				"ability": true,
				"traitTags": true
			},
			"hasFluff": true,
			"hasFluffImages": true,
			"_versions": [
				{
					"_template": {
						"name": "Dragonborn (Ravenite; {{color}})",
						"source": "EGW",
						"_mod": {
							"entries": [
								{
									"mode": "removeArr",
									"names": "Draconic Ancestry"
								},
								{
									"mode": "replaceArr",
									"replace": "Breath Weapon",
									"items": {
										"type": "entries",
										"name": "Breath Weapon",
										"entries": [
											"You can use your action to exhale destructive energy in a {{area}}.",
											"When you use your breath weapon, each creature in the area of the exhalation must make a {{savingThrow}} saving throw. The DC for this saving throw equals 8 + your Constitution modifier + your proficiency bonus. A creature takes {@damage 2d6} {{damageType}} damage on a failed save, and half as much damage on a successful one. The damage increases to {@damage 3d6} at 6th level, {@damage 4d6} at 11th level, and {@damage 5d6} at 16th level.",
											"After you use your breath weapon, you can't use it again until you complete a short or long rest."
										]
									}
								}
							]
						}
					},
					"_implementations": [
						{
							"_variables": {
								"color": "Black",
								"damageType": "acid",
								"area": "5-foot-wide, 30-foot-long line",
								"savingThrow": "Dexterity"
							}
						},
						{
							"_variables": {
								"color": "Blue",
								"damageType": "lightning",
								"area": "5-foot-wide, 30-foot-long line",
								"savingThrow": "Dexterity"
							}
						},
						{
							"_variables": {
								"color": "Brass",
								"damageType": "fire",
								"area": "5-foot-wide, 30-foot-long line",
								"savingThrow": "Dexterity"
							}
						},
						{
							"_variables": {
								"color": "Bronze",
								"damageType": "lightning",
								"area": "5-foot-wide, 30-foot-long line",
								"savingThrow": "Dexterity"
							}
						},
						{
							"_variables": {
								"color": "Copper",
								"damageType": "acid",
								"area": "5-foot-wide, 30-foot-long line",
								"savingThrow": "Dexterity"
							}
						},
						{
							"_variables": {
								"color": "Gold",
								"damageType": "fire",
								"area": "15-foot cone",
								"savingThrow": "Dexterity"
							}
						},
						{
							"_variables": {
								"color": "Green",
								"damageType": "poison",
								"area": "15-foot cone",
								"savingThrow": "Constitution"
							}
						},
						{
							"_variables": {
								"color": "Red",
								"damageType": "fire",
								"area": "15-foot cone",
								"savingThrow": "Dexterity"
							}
						},
						{
							"_variables": {
								"color": "Silver",
								"damageType": "cold",
								"area": "15-foot cone",
								"savingThrow": "Constitution"
							}
						},
						{
							"_variables": {
								"color": "White",
								"damageType": "cold",
								"area": "15-foot cone",
								"savingThrow": "Constitution"
							}
						}
					]
				}
			]
		},
		{
			"name": "Duergar",
			"source": "MTF",
			"raceName": "Dwarf",
			"raceSource": "PHB",
			"page": 81,
			"otherSources": [
				{
					"source": "SCAG",
					"page": 104
				}
			],
			"reprintedAs": [
				"Duergar|MPMM"
			],
			"ability": [
				{
					"str": 1
				}
			],
			"darkvision": 120,
			"traitTags": [
				"Sunlight Sensitivity"
			],
			"languageProficiencies": [
				{
					"common": true,
					"dwarvish": true,
					"undercommon": true
				}
			],
			"additionalSpells": [
				{
					"innate": {
						"3": {
							"daily": {
								"1": [
									"enlarge/reduce"
								]
							}
						},
						"5": {
							"daily": {
								"1": [
									"invisibility"
								]
							}
						}
					},
					"ability": "int"
				}
			],
			"entries": [
				{
					"name": "Superior Darkvision",
					"entries": [
						"Accustomed to life underground, you have superior vision in dark and dim conditions. You can see in dim light within 120 feet of you as if it were bright light, and in darkness as if it were dim light. You can't discern color in darkness, only shades of gray."
					],
					"data": {
						"overwrite": "Darkvision"
					},
					"type": "entries"
				},
				{
					"name": "Duergar Resilience",
					"entries": [
						"You have advantage on saving throws against poison, and you have resistance against poison damage. You also have advantage on saving throws against illusions and against being {@condition charmed} or {@condition paralyzed}."
					],
					"data": {
						"overwrite": "Dwarven Resilience"
					},
					"type": "entries"
				},
				{
					"name": "Languages",
					"entries": [
						"You can speak, read, and write Common, Dwarvish, and Undercommon."
					],
					"data": {
						"overwrite": "Languages"
					},
					"type": "entries"
				},
				{
					"name": "Duergar Magic",
					"entries": [
						"When you reach 3rd level, you can cast the {@spell Enlarge/Reduce} spell on yourself once with this trait, using only the spell's enlarge option. When you reach 5th level, you can cast the {@spell Invisibility} spell on yourself once with this trait. You don't need material components for either spell, and you can't cast them while you're in direct sunlight, although sunlight has no effect on them once cast. You regain the ability to cast these spells with this trait when you finish a long rest. Intelligence is your spellcasting ability for these spells."
					],
					"type": "entries"
				},
				{
					"name": "Sunlight Sensitivity",
					"entries": [
						"You have disadvantage on attack rolls and Wisdom ({@skill Perception}) checks that rely on sight when you, the target of your attack, or whatever you are trying to perceive is in direct sunlight."
					],
					"type": "entries"
				}
			],
			"overwrite": {
				"languageProficiencies": true
			},
			"hasFluff": true,
			"hasFluffImages": false
		},
		{
			"name": "Hill",
			"source": "PHB",
			"raceName": "Dwarf",
			"raceSource": "PHB",
			"page": 20,
			"srd": true,
			"basicRules": true,
			"ability": [
				{
					"wis": 1
				}
			],
			"heightAndWeight": {
				"baseHeight": 44,
				"heightMod": "2d4",
				"baseWeight": 115,
				"weightMod": "2d6"
			},
			"entries": [
				{
					"name": "Dwarven Toughness",
					"entries": [
						"Your hit point maximum increases by 1, and it increases by 1 every time you gain a level."
					],
					"type": "entries"
				}
			],
			"hasFluff": true,
			"hasFluffImages": true
		},
		{
			"name": "Mark of Warding",
			"source": "ERLW",
			"raceName": "Dwarf",
			"raceSource": "PHB",
			"page": 51,
			"otherSources": [
				{
					"source": "UAWGE",
					"page": 108
				}
			],
			"ability": [
				{
					"int": 1
				}
			],
			"traitTags": [
				"Dragonmark",
				"Skill Bonus Dice",
				"Tool Bonus Dice"
			],
			"additionalSpells": [
				{
					"expanded": {
						"s1": [
							"alarm",
							"armor of agathys"
						],
						"s2": [
							"arcane lock",
							"knock"
						],
						"s3": [
							"glyph of warding",
							"magic circle"
						],
						"s4": [
							"leomund's secret chest",
							"mordenkainen's faithful hound"
						],
						"s5": [
							"antilife shell"
						]
					},
					"ability": "int",
					"known": {
						"1": [
							"alarm",
							"mage armor"
						]
					}
				}
			],
			"entries": [
				{
					"type": "entries",
					"name": "Warder's Intuition",
					"entries": [
						"When you make an Intelligence ({@skill Investigation}) check or an ability check using {@item thieves' tools|PHB}, you can roll a {@dice d4} and add the number rolled to the ability check."
					]
				},
				{
					"type": "entries",
					"name": "Wards and Seals",
					"entries": [
						"You can cast the {@spell alarm} and {@spell mage armor} spells with this trait. Starting at 3rd level, you can also cast the {@spell arcane lock} spell with it. Once you cast any of these spells with this trait, you can't cast that spell with it again until you finish a long rest. Intelligence is your spellcasting ability for these spells, and you don't need material components for them when you cast them with this trait."
					]
				},
				{
					"type": "entries",
					"name": "Spells of the Mark",
					"entries": [
						"If you have the Spellcasting or the Pact Magic class feature, the spells on the Mark of Warding Spells table are added to the spell list of your spellcasting class.",
						{
							"type": "table",
							"caption": "Mark of Warding Spells",
							"colLabels": [
								"Spell Level",
								"Spells"
							],
							"colStyles": [
								"col-2 text-center",
								"col-10"
							],
							"rows": [
								[
									"1st",
									"{@spell alarm}, {@spell armor of Agathys}"
								],
								[
									"2nd",
									"{@spell arcane lock}, {@spell knock}"
								],
								[
									"3rd",
									"{@spell glyph of warding}, {@spell magic circle}"
								],
								[
									"4th",
									"{@spell Leomund's secret chest}, {@spell Mordenkainen's faithful hound}"
								],
								[
									"5th",
									"{@spell antilife shell}"
								]
							]
						}
					]
				}
			]
		},
		{
			"name": "Mountain",
			"source": "PHB",
			"raceName": "Dwarf",
			"raceSource": "PHB",
			"page": 20,
			"basicRules": true,
			"ability": [
				{
					"str": 2
				}
			],
			"heightAndWeight": {
				"baseHeight": 48,
				"heightMod": "2d4",
				"baseWeight": 130,
				"weightMod": "2d6"
			},
			"armorProficiencies": [
				{
					"light": true,
					"medium": true
				}
			],
			"entries": [
				{
					"name": "Dwarven Armor Training",
					"entries": [
						"You have proficiency with light and medium armor."
					],
					"type": "entries"
				}
			],
			"hasFluff": true,
			"hasFluffImages": true
		},
		{
			"name": "Avariel",
			"source": "UAElfSubraces",
			"raceName": "Elf",
			"raceSource": "PHB",
			"page": 1,
			"speed": {
				"walk": 30,
				"fly": 30
			},
			"languageProficiencies": [
				{
					"auran": true
				}
			],
			"entries": [
				{
					"name": "Extra Language",
					"entries": [
						"You can speak, read, and write Auran."
					],
					"type": "entries"
				},
				{
					"name": "Flight",
					"entries": [
						"You have a flying speed of 30 feet. To use this speed, you can't be wearing medium or heavy armor."
					],
					"type": "entries"
				}
			]
		},
		{
			"name": "Drow",
			"alias": [
				"Dark"
			],
			"source": "PHB",
			"raceName": "Elf",
			"raceSource": "PHB",
			"page": 24,
			"ability": [
				{
					"cha": 1
				}
			],
			"heightAndWeight": {
				"baseHeight": 53,
				"heightMod": "2d6",
				"baseWeight": 75,
				"weightMod": "1d6"
			},
			"darkvision": 120,
			"traitTags": [
				"Sunlight Sensitivity"
			],
			"weaponProficiencies": [
				{
					"rapier|phb": true,
					"shortsword|phb": true,
					"hand crossbow|phb": true
				}
			],
			"additionalSpells": [
				{
					"innate": {
						"3": {
							"daily": {
								"1": [
									"faerie fire"
								]
							}
						},
						"5": {
							"daily": {
								"1": [
									"darkness"
								]
							}
						}
					},
					"ability": "cha",
					"known": {
						"1": [
							"dancing lights#c"
						]
					}
				}
			],
			"entries": [
				{
					"name": "Superior Darkvision",
					"entries": [
						"Accustomed to the depths of the Underdark, you have superior vision in dark and dim conditions. You can see in dim light within 120 feet of you as if it were bright light, and in darkness as if it were dim light. You can't discern color in darkness, only shades of gray."
					],
					"data": {
						"overwrite": "Darkvision"
					},
					"type": "entries"
				},
				{
					"name": "Sunlight Sensitivity",
					"entries": [
						"You have disadvantage on attack rolls and on Wisdom ({@skill Perception}) checks that rely on sight when you, the target of your attack, or whatever you are trying to perceive is in direct sunlight."
					],
					"type": "entries"
				},
				{
					"name": "Drow Magic",
					"entries": [
						"You know the {@spell dancing lights} cantrip. When you reach 3rd level, you can cast the {@spell faerie fire} spell once with this trait; you regain the ability to cast it when you finish a long rest. When you reach 5th level, you can also cast the {@spell darkness} spell once per day with this trait; you regain the ability to cast it when you finish a long rest. Charisma is your spellcasting ability for these spells."
					],
					"type": "entries"
				},
				{
					"name": "Drow Weapon Training",
					"entries": [
						"You have proficiency with {@item rapier|phb|rapiers}, {@item shortsword|phb|shortswords}, and {@item hand crossbow|phb|hand crossbows}."
					],
					"type": "entries"
				}
			],
			"hasFluff": true
		},
		{
			"name": "Eladrin",
			"source": "DMG",
			"raceName": "Elf",
			"raceSource": "PHB",
			"page": 286,
			"ability": [
				{
					"int": 1
				}
			],
			"weaponProficiencies": [
				{
					"longsword|phb": true,
					"shortsword|phb": true,
					"shortbow|phb": true,
					"longbow|phb": true
				}
			],
			"additionalSpells": [
				{
					"ability": "cha",
					"known": {
						"1": {
							"rest": {
								"1": [
									"misty step"
								]
							}
						}
					}
				}
			],
			"entries": [
				{
					"name": "Elf Weapon Training",
					"entries": [
						"You have proficiency with the {@item longsword|phb}, {@item shortsword|phb}, {@item shortbow|phb}, and {@item longbow|phb}."
					],
					"type": "entries"
				},
				{
					"name": "Fey Step",
					"entries": [
						"You can cast the {@spell misty step} spell once using this trait. You regain the ability to do so when you finish a short or long rest."
					],
					"type": "entries"
				}
			]
		},
		{
			"name": "Eladrin",
			"source": "MTF",
			"raceName": "Elf",
			"raceSource": "PHB",
			"page": 61,
			"reprintedAs": [
				"Eladrin|MPMM"
			],
			"ability": [
				{
					"cha": 1
				}
			],
			"heightAndWeight": {
				"baseHeight": 54,
				"heightMod": "2d12",
				"baseWeight": 90,
				"weightMod": "1d4"
			},
			"entries": [
				"{@i Choose your eladrin's season: autumn, winter, spring, or summer. When finishing a long rest, you can change your season. See the \"Info\" tab for more information.}",
				{
					"name": "Fey Step",
					"entries": [
						"As a bonus action, you can magically teleport up to 30 feet to an unoccupied space you can see. Once you use this trait, you can't do so again until you finish a short or long rest.",
						"When you reach 3rd level, your Fey Step gains an additional effect based on your season; if the effect requires a saving throw, the DC equals 8 + your proficiency bonus + your Charisma modifier:",
						{
							"type": "list",
							"style": "list-hang-notitle",
							"items": [
								{
									"type": "item",
									"name": "Autumn",
									"entry": "Immediately after you use your Fey Step, up to two creatures of your choice that you can see within 10 feet of you must succeed on a Wisdom saving throw or be {@condition charmed} by you for 1 minute, or until you or your companions deal any damage to it."
								},
								{
									"type": "item",
									"name": "Winter",
									"entry": "When you use your Fey Step, one creature of your choice that you can see within 5 feet of you before you teleport must succeed on a Wisdom saving throw or be {@condition frightened} of you until the end of your next turn."
								},
								{
									"type": "item",
									"name": "Spring",
									"entry": "When you use your Fey Step, you can touch one willing creature within 5 feet of you. That creature then teleports instead of you, appearing in an unoccupied space of your choice that you can see within 30 feet of you."
								},
								{
									"type": "item",
									"name": "Summer",
									"entry": "Immediately after you use your Fey Step, each creature of your choice that you can see within 5 feet of you takes fire damage equal to your Charisma modifier (minimum of 1 damage)."
								}
							]
						}
					],
					"type": "entries"
				}
			],
			"hasFluff": true,
			"hasFluffImages": true
		},
		{
			"name": "Eladrin",
			"source": "UAEladrinAndGith",
			"raceName": "Elf",
			"raceSource": "PHB",
			"page": 1,
			"reprintedAs": [
				"Elf (Eladrin)|MTF"
			],
			"ability": [
				{
					"choose": {
						"from": [
							"int",
							"cha"
						],
						"count": 1
					}
				}
			],
			"additionalSpells": [
				{
					"known": {
						"1": [
							"friends#c",
							"chill touch#c",
							"minor illusion#c",
							"fire bolt#c"
						]
					}
				}
			],
			"entries": [
				{
					"name": "Fey Step",
					"entries": [
						"As a bonus action, you can magically teleport up to 30 feet to an unoccupied space you can see. Once you use this trait, you can't do so again until you finish a short or long rest."
					],
					"type": "entries"
				},
				{
					"name": "Shifting Seasons",
					"entries": [
						"At the end of each short or long rest, you can align yourself with the magic of one season, regardless of the season that is dominating your personality. Doing so allows you to cast a certain cantrip, as shown in the Shifting Seasons Cantrips table. When you align yourself with a season's magic, you lose the cantrip associated with the previous season and gain the cantrip associated with the new season.",
						"Your spellcasting ability for these cantrips is Intelligence or Charisma, whichever is higher.",
						{
							"type": "table",
							"caption": "Shifting Seasons Cantrips",
							"colLabels": [
								"Season",
								"Cantrip"
							],
							"colStyles": [
								"col-6 text-center",
								"col-6 text-center"
							],
							"rows": [
								[
									"Autumn",
									"{@spell Friends}"
								],
								[
									"Winter",
									"{@spell Chill touch}"
								],
								[
									"Spring",
									"{@spell Minor illusion}"
								],
								[
									"Summer",
									"{@spell Fire bolt}"
								]
							]
						}
					],
					"type": "entries"
				}
			]
		},
		{
			"name": "Grugach",
			"source": "UAElfSubraces",
			"raceName": "Elf",
			"raceSource": "PHB",
			"page": 1,
			"ability": [
				{
					"str": 1
				}
			],
			"languageProficiencies": [
				{
					"sylvan": true,
					"elvish": true,
					"anyStandard": 1
				}
			],
			"weaponProficiencies": [
				{
					"spear|phb": true,
					"shortbow|phb": true,
					"longbow|phb": true,
					"net|phb": true
				}
			],
			"additionalSpells": [
				{
					"ability": "wis",
					"known": {
						"1": {
							"_": [
								{
									"choose": "level=0|class=Druid"
								}
							]
						}
					}
				}
			],
			"entries": [
				{
					"name": "Languages",
					"entries": [
						"You can speak, read, and write Sylvan, Elvish, and one extra language of your choice. Elvish is fluid, with subtle intonations and intricate grammar. Elven literature is rich and varied, and their songs and poems are famous among other races. Many bards learn their language so they can add Elvish ballads to their repertoires."
					],
					"data": {
						"overwrite": "Languages"
					},
					"type": "entries"
				},
				{
					"name": "Grugach Weapon Training",
					"entries": [
						"You have proficiency with the {@item spear|phb}, {@item shortbow|phb}, {@item longbow|phb}, and {@item net|phb}."
					],
					"type": "entries"
				},
				{
					"name": "Cantrip",
					"entries": [
						"You know one cantrip of your choice from the {@filter druid spell list|spells|class=druid|level=0}. Wisdom is your spellcasting ability for it."
					],
					"type": "entries"
				}
			],
			"overwrite": {
				"languageProficiencies": true
			}
		},
		{
			"name": "High",
			"source": "PHB",
			"raceName": "Elf",
			"raceSource": "PHB",
			"page": 23,
			"srd": true,
			"basicRules": true,
			"speed": 30,
			"ability": [
				{
					"int": 1
				}
			],
			"heightAndWeight": {
				"baseHeight": 54,
				"heightMod": "2d10",
				"baseWeight": 90,
				"weightMod": "1d4"
			},
			"languageProficiencies": [
				{
					"common": true,
					"elvish": true,
					"anyStandard": 1
				}
			],
			"weaponProficiencies": [
				{
					"longsword|phb": true,
					"shortsword|phb": true,
					"shortbow|phb": true,
					"longbow|phb": true
				}
			],
			"additionalSpells": [
				{
					"ability": "int",
					"known": {
						"1": {
							"_": [
								{
									"choose": "level=0|class=Wizard"
								}
							]
						}
					}
				}
			],
			"entries": [
				{
					"name": "Elf Weapon Training",
					"entries": [
						"You have proficiency with the {@item longsword|phb}, {@item shortsword|phb}, {@item shortbow|phb}, and {@item longbow|phb}."
					],
					"type": "entries"
				},
				{
					"name": "Cantrip",
					"entries": [
						"You know one {@filter cantrip of your choice from the wizard spell list|spells|level=0|class=Wizard}. Intelligence is your spellcasting ability for it."
					],
					"type": "entries"
				},
				{
					"name": "Extra Language",
					"entries": [
						"You can speak, read, and write one extra language of your choosing."
					],
					"type": "entries"
				}
			],
			"overwrite": {
				"languageProficiencies": true
			},
			"hasFluff": true,
			"hasFluffImages": true
		},
		{
			"name": "High; Aereni",
			"source": "UAWGE",
			"raceName": "Elf",
			"raceSource": "PHB",
			"page": 73,
			"speed": 30,
			"ability": [
				{
					"int": 1
				}
			],
			"traitTags": [
				"Skill Proficiency",
				"Tool Proficiency"
			],
			"skillToolLanguageProficiencies": [
				{
					"choose": [
						{
							"from": [
								"anySkill",
								"anyTool"
							]
						}
					]
				}
			],
			"additionalSpells": [
				{
					"ability": "int",
					"known": {
						"1": {
							"_": [
								{
									"choose": "level=0|class=Wizard"
								}
							]
						}
					}
				}
			],
			"entries": [
				{
					"name": "Aereni Training",
					"entries": [
						"Choose one skill or {@book tool|phb|5|tools} proficiency. Your proficiency bonus is doubled for any ability check you make that uses this chosen proficiency."
					],
					"type": "entries"
				},
				{
					"name": "Cantrip",
					"entries": [
						"You know one {@filter cantrip of your choice from the wizard spell list|spells|level=0|class=Wizard}. Intelligence is your spellcasting ability for it."
					],
					"type": "entries"
				},
				{
					"name": "Extra Language",
					"entries": [
						"You can speak, read, and write one extra language of your choosing."
					],
					"type": "entries"
				}
			]
		},
		{
			"name": "High; Valenar",
			"source": "UAWGE",
			"raceName": "Elf",
			"raceSource": "PHB",
			"page": 73,
			"speed": 30,
			"ability": [
				{
					"int": 1
				}
			],
			"weaponProficiencies": [
				{
					"scimitar|phb": true,
					"double-bladed scimitar|erlw": true,
					"longbow|phb": true,
					"shortbow|phb": true
				}
			],
			"additionalSpells": [
				{
					"ability": "int",
					"known": {
						"1": {
							"_": [
								{
									"choose": "level=0|class=Wizard"
								}
							]
						}
					}
				}
			],
			"entries": [
				{
					"name": "Valenar Weapon Training",
					"entries": [
						"A Valenar elf gains proficiency with the {@item scimitar|phb}, {@item Double-Bladed Scimitar|erlw|double scimitar}, {@item longbow|phb}, and {@item shortbow|phb}."
					],
					"type": "entries"
				},
				{
					"name": "Cantrip",
					"entries": [
						"You know one {@filter cantrip of your choice from the wizard spell list|spells|level=0|class=Wizard}. Intelligence is your spellcasting ability for it."
					],
					"type": "entries"
				},
				{
					"name": "Extra Language",
					"entries": [
						"You can speak, read, and write one extra language of your choosing."
					],
					"type": "entries"
				}
			]
		},
		{
			"name": "Mark of Shadow",
			"source": "ERLW",
			"raceName": "Elf",
			"raceSource": "PHB",
			"page": 49,
			"otherSources": [
				{
					"source": "UAWGE",
					"page": 105
				}
			],
			"ability": [
				{
					"cha": 1
				}
			],
			"traitTags": [
				"Dragonmark",
				"Skill Bonus Dice"
			],
			"additionalSpells": [
				{
					"innate": {
						"3": {
							"daily": {
								"1": [
									"invisibility"
								]
							}
						}
					},
					"expanded": {
						"s1": [
							"disguise self",
							"silent image"
						],
						"s2": [
							"darkness",
							"pass without trace"
						],
						"s3": [
							"clairvoyance",
							"major image"
						],
						"s4": [
							"greater invisibility",
							"hallucinatory terrain"
						],
						"s5": [
							"mislead"
						]
					},
					"ability": "cha",
					"known": {
						"1": [
							"minor illusion#c"
						]
					}
				}
			],
			"entries": [
				{
					"type": "entries",
					"name": "Cunning Intuition",
					"entries": [
						"When you make a Charisma ({@skill Performance}) or Dexterity ({@skill Stealth}) check, you can roll a {@dice d4} and add the number rolled to the ability check."
					]
				},
				{
					"type": "entries",
					"name": "Shape Shadows",
					"entries": [
						"You know the {@spell minor illusion} cantrip. Starting at 3rd level, you can cast the {@spell invisibility} spell once with this trait, and you regain the ability to cast it when you finish a long rest. Charisma is your spellcasting ability for these spells."
					]
				},
				{
					"type": "entries",
					"name": "Spells of the Mark",
					"entries": [
						"If you have the Spellcasting or the Pact Magic class feature, the spells on the Mark of Shadow Spells table are added to the spell list of your spellcasting class.",
						{
							"type": "table",
							"caption": "Mark of Shadow Spells",
							"colLabels": [
								"Spell Level",
								"Spells"
							],
							"colStyles": [
								"col-2 text-center",
								"col-10"
							],
							"rows": [
								[
									"1st",
									"{@spell disguise self}, {@spell silent image}"
								],
								[
									"2nd",
									"{@spell darkness}, {@spell pass without trace}"
								],
								[
									"3rd",
									"{@spell clairvoyance}, {@spell major image}"
								],
								[
									"4th",
									"{@spell greater invisibility}, {@spell hallucinatory terrain}"
								],
								[
									"5th",
									"{@spell mislead}"
								]
							]
						}
					]
				}
			]
		},
		{
			"name": "Pallid",
			"source": "EGW",
			"raceName": "Elf",
			"raceSource": "PHB",
			"page": 21,
			"ability": [
				{
					"wis": 1
				}
			],
			"heightAndWeight": {
				"baseHeight": 54,
				"heightMod": "2d10",
				"baseWeight": 90,
				"weightMod": "1d4"
			},
			"additionalSpells": [
				{
					"innate": {
						"3": {
							"daily": {
								"1": [
									"sleep"
								]
							}
						},
						"5": {
							"daily": {
								"1": [
									"invisibility"
								]
							}
						}
					},
					"ability": "wis",
					"known": {
						"1": [
							"light#c"
						]
					}
				}
			],
			"entries": [
				{
					"name": "Incisive Sense",
					"entries": [
						"You have advantage on Intelligence ({@skill Investigation}) and Wisdom ({@skill Insight}) checks."
					],
					"type": "entries"
				},
				{
					"type": "entries",
					"name": "Blessing of the Moon Weaver",
					"entries": [
						"You know the {@spell light} cantrip. When you reach 3rd level, you can cast the {@spell sleep} spell once with this trait and regain the ability to do so when you finish a long rest. When you reach 5th level, you can cast the {@spell invisibility} spell (targeting yourself only) once with this trait and regain the ability to do so when you finish a long rest. Casting these spells with this trait doesn't require material components. Wisdom is your spellcasting ability for these spells."
					]
				}
			],
			"hasFluff": true,
			"hasFluffImages": true
		},
		{
			"name": "Sea",
			"source": "MTF",
			"raceName": "Elf",
			"raceSource": "PHB",
			"page": 62,
			"otherSources": [
				{
					"source": "EGW",
					"page": 163
				}
			],
			"reprintedAs": [
				"Sea Elf|MPMM"
			],
			"speed": {
				"walk": 30,
				"swim": 30
			},
			"ability": [
				{
					"con": 1
				}
			],
			"heightAndWeight": {
				"baseHeight": 54,
				"heightMod": "2d8",
				"baseWeight": 90,
				"weightMod": "1d4"
			},
			"traitTags": [
				"Amphibious"
			],
			"languageProficiencies": [
				{
					"common": true,
					"elvish": true,
					"aquan": true
				}
			],
			"weaponProficiencies": [
				{
					"spear|phb": true,
					"trident|phb": true,
					"light crossbow|phb": true,
					"net|phb": true
				}
			],
			"entries": [
				{
					"name": "Sea Elf Training",
					"entries": [
						"You have proficiency with the {@item spear|phb}, {@item trident|phb}, {@item light crossbow|phb}, and {@item net|phb}."
					],
					"type": "entries"
				},
				{
					"name": "Child of the Sea",
					"entries": [
						"You have a swimming speed of 30 feet, and you can breathe air and water."
					],
					"type": "entries"
				},
				{
					"name": "Friend of the Sea",
					"entries": [
						"Using gestures and sounds, you can communicate simple ideas with any beast that has an innate swimming speed."
					],
					"type": "entries"
				},
				{
					"name": "Extra Language",
					"entries": [
						"You can speak, read, and write Aquan."
					],
					"type": "entries"
				}
			],
			"hasFluff": true
		},
		{
			"name": "Sea",
			"source": "UAElfSubraces",
			"raceName": "Elf",
			"raceSource": "PHB",
			"page": 1,
			"speed": {
				"walk": 30,
				"swim": 30
			},
			"ability": [
				{
					"con": 1
				}
			],
			"traitTags": [
				"Amphibious"
			],
			"languageProficiencies": [
				{
					"common": true,
					"elvish": true,
					"aquan": true
				}
			],
			"weaponProficiencies": [
				{
					"spear|phb": true,
					"trident|phb": true,
					"light crossbow|phb": true,
					"net|phb": true
				}
			],
			"entries": [
				{
					"name": "Extra Language",
					"entries": [
						"You can speak, read, and write Aquan."
					],
					"type": "entries"
				},
				{
					"name": "Sea Elf Weapon Training",
					"entries": [
						"You have proficiency with the {@item spear|phb}, {@item trident|phb}, {@item light crossbow|phb}, and {@item net|phb}."
					],
					"type": "entries"
				},
				{
					"name": "Child of the Sea",
					"entries": [
						"You have a swimming speed of 30 feet, and you can breathe air and water."
					],
					"type": "entries"
				},
				{
					"name": "Friend of the Sea",
					"entries": [
						"Using gestures and sounds, you can communicate simple ideas with Small or smaller beasts that have an inborn swimming speed."
					],
					"type": "entries"
				}
			]
		},
		{
			"name": "Shadar-kai",
			"source": "MTF",
			"raceName": "Elf",
			"raceSource": "PHB",
			"page": 62,
			"reprintedAs": [
				"Shadar-Kai|MPMM"
			],
			"ability": [
				{
					"con": 1
				}
			],
			"heightAndWeight": {
				"baseHeight": 56,
				"heightMod": "2d8",
				"baseWeight": 90,
				"weightMod": "1d4"
			},
			"resist": [
				"necrotic"
			],
			"entries": [
				{
					"type": "entries",
					"name": "Necrotic Resistance",
					"entries": [
						"You have resistance to necrotic damage."
					]
				},
				{
					"name": "Blessing of the Raven Queen",
					"entries": [
						"As a bonus action, you can magically teleport up to 30 feet to an unoccupied space you can see. Once you use this trait, you can't do so again until you finish a long rest.",
						"Starting at 3rd level, you also gain resistance to all damage when you teleport using this trait. The resistance lasts until the start of your next turn. During that time, you appear ghostly and translucent."
					],
					"type": "entries"
				}
			],
			"hasFluff": true
		},
		{
			"name": "Shadar-kai",
			"source": "UAElfSubraces",
			"raceName": "Elf",
			"raceSource": "PHB",
			"page": 2,
			"reprintedAs": [
				"Elf (Shadar-kai)|MTF"
			],
			"ability": [
				{
					"cha": 1
				}
			],
			"languageProficiencies": [
				{
					"common": true,
					"elvish": true,
					"anyStandard": 1
				}
			],
			"additionalSpells": [
				{
					"ability": "cha",
					"known": {
						"1": [
							"chill touch#c"
						]
					}
				},
				{
					"ability": "cha",
					"known": {
						"1": [
							"spare the dying#c"
						]
					}
				},
				{
					"ability": "cha",
					"known": {
						"1": [
							"thaumaturgy#c"
						]
					}
				}
			],
			"entries": [
				{
					"name": "Languages",
					"entries": [
						"You can speak, read, and write Common, Elvish, and one extra language of your choice. Elvish is fluid, with subtle intonations and intricate grammar. Elven literature is rich and varied, and their songs and poems are famous among other races. Many bards learn their language so they can add Elvish ballads to their repertoires."
					],
					"data": {
						"overwrite": "Languages"
					},
					"type": "entries"
				},
				{
					"name": "Cantrip",
					"entries": [
						"You know one of the following cantrips of your choice: {@spell chill touch}, {@spell spare the dying}, or {@spell thaumaturgy}. Charisma is your spellcasting ability for it."
					],
					"type": "entries"
				},
				{
					"name": "Blessing of the Raven Queen",
					"entries": [
						"As a bonus action, you can magically teleport up to 15 feet to an unoccupied space you can see, and you gain resistance to all damage until the start of your next turn. During that time, you appear ghostly and translucent. Once you use this ability, you can't use it again until you finish a short or long rest."
					],
					"type": "entries"
				}
			],
			"overwrite": {
				"languageProficiencies": true
			}
		},
		{
			"name": "Wood",
			"source": "PHB",
			"raceName": "Elf",
			"raceSource": "PHB",
			"page": 24,
			"basicRules": true,
			"speed": 35,
			"ability": [
				{
					"wis": 1
				}
			],
			"heightAndWeight": {
				"baseHeight": 54,
				"heightMod": "2d10",
				"baseWeight": 100,
				"weightMod": "1d4"
			},
			"weaponProficiencies": [
				{
					"longsword|phb": true,
					"shortsword|phb": true,
					"shortbow|phb": true,
					"longbow|phb": true
				}
			],
			"entries": [
				{
					"name": "Elf Weapon Training",
					"entries": [
						"You have proficiency with the {@item longsword|phb}, {@item shortsword|phb}, {@item shortbow|phb}, and {@item longbow|phb}."
					],
					"type": "entries"
				},
				{
					"name": "Fleet of Foot",
					"entries": [
						"Your base walking speed increases to 35 feet."
					],
					"type": "entries"
				},
				{
					"name": "Mask of the Wild",
					"entries": [
						"You can attempt to hide even when you are only lightly obscured by foliage, heavy rain, falling snow, mist, and other natural phenomena."
					],
					"type": "entries"
				}
			],
			"hasFluff": true,
			"hasFluffImages": true
		},
		{
			"name": "Wood; Aereni",
			"source": "UAWGE",
			"raceName": "Elf",
			"raceSource": "PHB",
			"page": 73,
			"speed": 35,
			"ability": [
				{
					"wis": 1
				}
			],
			"entries": [
				{
					"name": "Aereni Training",
					"entries": [
						"Choose one skill or {@book tool|phb|5|tools} proficiency. Your proficiency bonus is doubled for any ability check you make that uses this chosen proficiency."
					],
					"type": "entries"
				},
				{
					"name": "Fleet of Foot",
					"entries": [
						"Your base walking speed increases to 35 feet."
					],
					"type": "entries"
				},
				{
					"name": "Mask of the Wild",
					"entries": [
						"You can attempt to hide even when you are only lightly obscured by foliage, heavy rain, falling snow, mist, and other natural phenomena."
					],
					"type": "entries"
				}
			]
		},
		{
			"name": "Wood; Valenar",
			"source": "UAWGE",
			"raceName": "Elf",
			"raceSource": "PHB",
			"page": 73,
			"speed": 35,
			"ability": [
				{
					"wis": 1
				}
			],
			"weaponProficiencies": [
				{
					"scimitar|phb": true,
					"double-bladed scimitar|erlw": true,
					"longbow|phb": true,
					"shortbow|phb": true
				}
			],
			"entries": [
				{
					"name": "Valenar Weapon Training",
					"entries": [
						"A Valenar elf gains proficiency with the {@item scimitar|phb}, {@item Double-Bladed Scimitar|erlw|double scimitar}, {@item longbow|phb}, and {@item shortbow|phb}."
					],
					"type": "entries"
				},
				{
					"name": "Fleet of Foot",
					"entries": [
						"Your base walking speed increases to 35 feet."
					],
					"type": "entries"
				},
				{
					"name": "Mask of the Wild",
					"entries": [
						"You can attempt to hide even when you are only lightly obscured by foliage, heavy rain, falling snow, mist, and other natural phenomena."
					],
					"type": "entries"
				}
			]
		},
		{
			"name": "Bishatar and Tirahar",
			"source": "PSK",
			"raceName": "Elf (Kaladesh)",
			"raceSource": "PSK",
			"page": 21,
			"speed": 35,
			"entries": [
				{
					"name": "Fleet of Foot",
					"entries": [
						"Your ground speed increases to 35 feet."
					],
					"type": "entries"
				},
				{
					"name": "Mask of the Wild",
					"entries": [
						"You can attempt to hide even when you are only lightly obscured by foliage, heavy rain, falling snow, mist, and other natural phenomena."
					],
					"type": "entries"
				}
			],
			"hasFluff": true,
			"hasFluffImages": true
		},
		{
			"name": "Vahadar",
			"source": "PSK",
			"raceName": "Elf (Kaladesh)",
			"raceSource": "PSK",
			"page": 21,
			"additionalSpells": [
				{
					"ability": "wis",
					"known": {
						"1": {
							"_": [
								{
									"choose": "level=0|class=Druid"
								}
							]
						}
					}
				}
			],
			"entries": [
				{
					"name": "Cantrip",
					"entries": [
						"You know one cantrip of your choice from the {@filter druid spell list|spells|class=druid|level=0}. Wisdom is your spellcasting ability for it."
					],
					"type": "entries"
				},
				{
					"name": "Extra Language",
					"entries": [
						"You can speak, read, and write one extra language of your choosing."
					],
					"type": "entries"
				}
			],
			"hasFluff": true,
			"hasFluffImages": true
		},
		{
			"name": "Joraga Nation",
			"source": "PSZ",
			"raceName": "Elf (Zendikar)",
			"raceSource": "PSZ",
			"page": 19,
			"speed": 35,
			"ability": [
				{
					"dex": 1
				}
			],
			"weaponProficiencies": [
				{
					"longsword|phb": true,
					"shortsword|phb": true,
					"shortbow|phb": true,
					"longbow|phb": true
				}
			],
			"entries": [
				{
					"name": "Mask of the Wild",
					"entries": [
						"You can attempt to hide even when you are only lightly obscured by foliage, heavy rain, falling snow, mist, and other natural phenomena."
					],
					"type": "entries"
				},
				{
					"name": "Elf Weapon Training",
					"entries": [
						"You have proficiency with the {@item longsword|phb}, {@item shortsword|phb}, {@item shortbow|phb}, and {@item longbow|phb}."
					],
					"type": "entries"
				},
				{
					"name": "Fleet of Foot",
					"entries": [
						"Your ground speed increases to 35 feet."
					],
					"type": "entries"
				}
			],
			"hasFluff": true,
			"hasFluffImages": true
		},
		{
			"name": "Mul Daya Nation",
			"source": "PSZ",
			"raceName": "Elf (Zendikar)",
			"raceSource": "PSZ",
			"page": 19,
			"ability": [
				{
					"str": 1
				}
			],
			"darkvision": 120,
			"traitTags": [
				"Sunlight Sensitivity"
			],
			"weaponProficiencies": [
				{
					"longsword|phb": true,
					"shortsword|phb": true,
					"shortbow|phb": true,
					"longbow|phb": true
				}
			],
			"additionalSpells": [
				{
					"innate": {
						"3": {
							"daily": {
								"1": [
									"hex"
								]
							}
						},
						"5": {
							"daily": {
								"1": [
									"darkness"
								]
							}
						}
					},
					"ability": "wis",
					"known": {
						"1": [
							"chill touch#c"
						]
					}
				}
			],
			"entries": [
				{
					"name": "Mul Daya Magic",
					"entries": [
						"You know the {@spell chill touch} cantrip. When you reach 3rd level, you can cast the {@spell hex} spell once with this trait and regain the ability to do so when you finish a long rest. When you reach 5th level, you can cast the {@spell darkness} spell once with this trait and regain the ability to do so when you finish a long rest. Wisdom is your spellcasting ability for these spells."
					],
					"type": "entries"
				},
				{
					"name": "Superior Darkvision",
					"entries": [
						"Your Darkvision has a radius of 120 feet."
					],
					"data": {
						"overwrite": "Darkvision"
					},
					"type": "entries"
				},
				{
					"name": "Sunlight Sensitivity",
					"entries": [
						"You have disadvantage on attack rolls and on Wisdom ({@skill Perception}) checks that rely on sight when you, the target of your attack, or whatever you are trying to perceive is in direct sunlight."
					],
					"type": "entries"
				},
				{
					"name": "Elf Weapon Training",
					"entries": [
						"You have proficiency with the {@item longsword|phb}, {@item shortsword|phb}, {@item shortbow|phb}, and {@item longbow|phb}."
					],
					"type": "entries"
				}
			],
			"hasFluff": true,
			"hasFluffImages": true
		},
		{
			"name": "Tajuru Nation",
			"source": "PSZ",
			"raceName": "Elf (Zendikar)",
			"raceSource": "PSZ",
			"page": 18,
			"ability": [
				{
					"cha": 1
				}
			],
			"traitTags": [
				"Skill Proficiency",
				"Tool Proficiency"
			],
			"skillToolLanguageProficiencies": [
				{
					"choose": [
						{
							"from": [
								"anySkill",
								"anyTool"
							],
							"count": 2
						}
					]
				}
			],
			"entries": [
				{
					"name": "Skill Versatility",
					"entries": [
						"You have proficiency with any combination of two other skills or {@book tools|phb|5|tools} of your choice."
					],
					"type": "entries"
				}
			],
			"hasFluff": true,
			"hasFluffImages": true
		},
		{
			"name": "Air",
			"source": "EEPC",
			"raceName": "Genasi",
			"raceSource": "EEPC",
			"page": 9,
			"reprintedAs": [
				"Genasi (Air)|MPMM"
			],
			"ability": [
				{
					"dex": 1
				}
			],
			"additionalSpells": [
				{
					"ability": "con",
					"known": {
						"1": [
							"levitate"
						]
					}
				}
			],
			"entries": [
				{
					"name": "Unending Breath",
					"entries": [
						"You can hold your breath indefinitely while you're not {@condition incapacitated}."
					],
					"type": "entries"
				},
				{
					"name": "Mingle with the Wind",
					"entries": [
						"You can cast the {@spell levitate} spell once with this trait, requiring no material components, and you regain the ability to cast it this way when you finish a long rest. Constitution is your spellcasting ability for this spell."
					],
					"type": "entries"
				}
			],
			"hasFluff": true,
			"hasFluffImages": true
		},
		{
			"name": "Earth",
			"source": "EEPC",
			"raceName": "Genasi",
			"raceSource": "EEPC",
			"page": 9,
			"reprintedAs": [
				"Genasi (Earth)|MPMM"
			],
			"ability": [
				{
					"str": 1
				}
			],
			"additionalSpells": [
				{
					"ability": "con",
					"known": {
						"1": [
							"pass without trace"
						]
					}
				}
			],
			"entries": [
				{
					"name": "Earth Walk",
					"entries": [
						"You can move across {@quickref difficult terrain||3} made of earth or stone without expending extra movement."
					],
					"type": "entries"
				},
				{
					"name": "Merge with Stone",
					"entries": [
						"You can cast the {@spell pass without trace} spell once with this trait, requiring no material components, and you regain the ability to cast it this way when you finish a long rest. Constitution is your spellcasting ability for this spell."
					],
					"type": "entries"
				}
			],
			"hasFluff": true,
			"hasFluffImages": true
		},
		{
			"name": "Fire",
			"source": "EEPC",
			"raceName": "Genasi",
			"raceSource": "EEPC",
			"page": 9,
			"reprintedAs": [
				"Genasi (Fire)|MPMM"
			],
			"ability": [
				{
					"int": 1
				}
			],
			"darkvision": 60,
			"resist": [
				"fire"
			],
			"additionalSpells": [
				{
					"innate": {
						"3": {
							"daily": {
								"1": [
									"burning hands"
								]
							}
						}
					},
					"ability": "con",
					"known": {
						"1": [
							"produce flame#c"
						]
					}
				}
			],
			"entries": [
				{
					"name": "Darkvision",
					"entries": [
						"You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. Your ties to the Elemental Plane of Fire make your darkvision unusual: everything you see in darkness is in a shade of red."
					],
					"type": "entries"
				},
				{
					"name": "Fire Resistance",
					"entries": [
						"You have resistance to fire damage."
					],
					"type": "entries"
				},
				{
					"name": "Reach to the Blaze",
					"entries": [
						"You know the {@spell produce flame} cantrip. Once you reach 3rd level, you can cast the {@spell burning hands} spell once with this trait as a 1st-level spell, and you regain the ability to cast it this way when you finish a long rest. Constitution is your spellcasting ability for these spells."
					],
					"type": "entries"
				}
			],
			"hasFluff": true,
			"hasFluffImages": true
		},
		{
			"name": "Water",
			"source": "EEPC",
			"raceName": "Genasi",
			"raceSource": "EEPC",
			"page": 10,
			"reprintedAs": [
				"Genasi (Water)|MPMM"
			],
			"speed": {
				"walk": 30,
				"swim": 30
			},
			"ability": [
				{
					"wis": 1
				}
			],
			"traitTags": [
				"Amphibious"
			],
			"resist": [
				"acid"
			],
			"additionalSpells": [
				{
					"innate": {
						"3": {
							"daily": {
								"1": [
									"create or destroy water#2"
								]
							}
						}
					},
					"ability": "con",
					"known": {
						"1": [
							"shape water|xge#c"
						]
					}
				}
			],
			"entries": [
				{
					"name": "Acid Resistance",
					"entries": [
						"You have resistance to acid damage."
					],
					"type": "entries"
				},
				{
					"name": "Amphibious",
					"entries": [
						"You can breathe air and water."
					],
					"type": "entries"
				},
				{
					"name": "Swim",
					"entries": [
						"You have a swimming speed of 30 feet."
					],
					"type": "entries"
				},
				{
					"name": "Call to the Wave",
					"entries": [
						"You know the {@spell shape water|xge} cantrip. When you reach 3rd level, you can cast the {@spell create or destroy water} spell as a 2nd-level spell once with this trait, and you regain the ability to cast it this way when you finish a long rest. Constitution is your spellcasting ability for these spells."
					],
					"type": "entries"
				}
			],
			"hasFluff": true,
			"hasFluffImages": true
		},
		{
			"name": "Air",
			"source": "MPMM",
			"raceName": "Genasi",
			"raceSource": "MPMM",
			"page": 16,
			"speed": 35,
			"resist": [
				"lightning"
			],
			"additionalSpells": [
				{
					"innate": {
						"3": {
							"daily": {
								"1": [
									"feather fall"
								]
							}
						},
						"5": {
							"daily": {
								"1": [
									"levitate"
								]
							}
						}
					},
					"ability": {
						"choose": [
							"int",
							"wis",
							"cha"
						]
					},
					"known": {
						"1": [
							"shocking grasp#c"
						]
					}
				}
			],
			"entries": [
				{
					"type": "entries",
					"name": "Unending Breath",
					"entries": [
						"You can hold your breath indefinitely while you're not {@condition incapacitated}."
					]
				},
				{
					"type": "entries",
					"name": "Lightning Resistance",
					"entries": [
						"You have resistance to lightning damage."
					]
				},
				{
					"type": "entries",
					"name": "Mingle with the Wind",
					"entries": [
						"You know the {@spell shocking grasp} cantrip. Starting at 3rd level, you can cast the {@spell feather fall} spell with this trait, without requiring a material component. Starting 5th level, you can also cast the {@spell levitate} spell with this trait, without requiring a material component. Once you cast {@spell feather fall} or {@spell levitate} with this trait, you can't cast that spell with it again until you finish a long rest. You can also cast either of those spells using any spell slots you have of the appropriate level.",
						"Intelligence, Wisdom, or Charisma is your spellcasting ability for these spells when you cast them with this trait (choose when you select this race)."
					]
				}
			],
			"hasFluff": true,
			"hasFluffImages": true
		},
		{
			"name": "Earth",
			"source": "MPMM",
			"raceName": "Genasi",
			"raceSource": "MPMM",
			"page": 17,
			"additionalSpells": [
				{
					"innate": {
						"5": [
							"pass without trace"
						]
					},
					"ability": {
						"choose": [
							"int",
							"wis",
							"cha"
						]
					},
					"known": {
						"1": [
							"blade ward#c"
						]
					}
				}
			],
			"entries": [
				{
					"type": "entries",
					"name": "Earth Walk",
					"entries": [
						"You can move across {@quickref difficult terrain||3} without expending extra movement if you are using your walking speed on the ground or a floor."
					]
				},
				{
					"type": "entries",
					"name": "Merge with Stone",
					"entries": [
						"You know the {@spell blade ward} cantrip. You can cast it as normal, and you can also cast it as a bonus action a number of times equal to your proficiency bonus, regaining all expended uses when you finish a long rest.",
						"Starting at 5th level, you can cast the {@spell pass without trace} spell with this trait, without requiring a material component. Once you cast that spell with this trait, you can't do so again until you finish a long rest. You can also cast it using any spell slots you have of 2nd level or higher.",
						"Intelligence, Wisdom, or Charisma is your spellcasting ability for these spells when you cast them with this trait (choose when you select this race)."
					]
				}
			],
			"hasFluff": true,
			"hasFluffImages": true
		},
		{
			"name": "Fire",
			"source": "MPMM",
			"raceName": "Genasi",
			"raceSource": "MPMM",
			"page": 17,
			"resist": [
				"fire"
			],
			"additionalSpells": [
				{
					"innate": {
						"3": {
							"daily": {
								"1": [
									"burning hands"
								]
							}
						},
						"5": {
							"daily": {
								"1": [
									"flame blade"
								]
							}
						}
					},
					"ability": {
						"choose": [
							"int",
							"wis",
							"cha"
						]
					},
					"known": {
						"1": [
							"produce flame#c"
						]
					}
				}
			],
			"entries": [
				{
					"type": "entries",
					"name": "Fire Resistance",
					"entries": [
						"You have resistance to fire damage."
					]
				},
				{
					"type": "entries",
					"name": "Reach to the Blaze",
					"entries": [
						"You know the {@spell produce flame} cantrip. Starting at 3rd level, you can cast the {@spell burning hands} spell with this trait. Starting at 5th level, you can also cast the {@spell flame blade} spell with this trait, without a material component. Once you cast {@spell burning hands} or {@spell flame blade} with this trait, you can't cast that spell with it again until you finish a long rest. You can also cast either of those spells using any spell slots you have of the appropriate level.",
						"Intelligence, Wisdom, or Charisma is your spellcasting ability for these spells when you cast them with this trait (choose when you select this race)."
					]
				}
			],
			"hasFluff": true,
			"hasFluffImages": true
		},
		{
			"name": "Water",
			"source": "MPMM",
			"raceName": "Genasi",
			"raceSource": "MPMM",
			"page": 17,
			"speed": {
				"walk": 30,
				"swim": true
			},
			"traitTags": [
				"Amphibious"
			],
			"resist": [
				"acid"
			],
			"additionalSpells": [
				{
					"innate": {
						"3": {
							"daily": {
								"1": [
									"create or destroy water"
								]
							}
						},
						"5": {
							"daily": {
								"1": [
									"water walk"
								]
							}
						}
					},
					"ability": {
						"choose": [
							"int",
							"wis",
							"cha"
						]
					},
					"known": {
						"1": [
							"acid splash#c"
						]
					}
				}
			],
			"entries": [
				{
					"type": "entries",
					"name": "Speed",
					"entries": [
						"Your walking speed is 30 feet, and you have a swimming speed equal to your walking speed."
					]
				},
				{
					"type": "entries",
					"name": "Acid Resistance",
					"entries": [
						"You have resistance to acid damage."
					]
				},
				{
					"type": "entries",
					"name": "Amphibious",
					"entries": [
						"You breathe air and water."
					]
				},
				{
					"type": "entries",
					"name": "Call to the Wave",
					"entries": [
						"You know the {@spell acid splash} cantrip. Starting at 3rd level, you can cast the {@spell create or destroy water} spell with this trait. Starting at 5th level, you can also cast the {@spell water walk} spell with this trait, without requiring a material component. Once you cast {@spell create or destroy water} or {@spell water walk} with this trait, you can't cast that spell with it again until you finish a long rest. You can also cast either of those spells using any spell slots you have of the appropriate level.",
						"Intelligence, Wisdom, or Charisma is your spellcasting ability for these spells when you cast them with this trait (choose when you select this race)."
					]
				}
			],
			"hasFluff": true,
			"hasFluffImages": true
		},
		{
			"name": "Githyanki",
			"source": "MTF",
			"raceName": "Gith",
			"raceSource": "MTF",
			"page": 96,
			"reprintedAs": [
				"Githyanki|MPMM"
			],
			"ability": [
				{
					"str": 2
				}
			],
			"heightAndWeight": {
				"baseHeight": 60,
				"heightMod": "2d12",
				"baseWeight": 100,
				"weightMod": "2d4"
			},
			"traitTags": [
				"Skill Proficiency",
				"Tool Proficiency"
			],
			"weaponProficiencies": [
				{
					"shortsword|phb": true,
					"longsword|phb": true,
					"greatsword|phb": true
				}
			],
			"armorProficiencies": [
				{
					"light": true,
					"medium": true
				}
			],
			"skillToolLanguageProficiencies": [
				{
					"choose": [
						{
							"from": [
								"anySkill",
								"anyTool"
							]
						}
					]
				}
			],
			"additionalSpells": [
				{
					"innate": {
						"3": {
							"daily": {
								"1": [
									"jump"
								]
							}
						},
						"5": {
							"daily": {
								"1": [
									"misty step"
								]
							}
						}
					},
					"ability": "int",
					"known": {
						"1": [
							"mage hand#c"
						]
					}
				}
			],
			"entries": [
				{
					"name": "Alignment",
					"type": "entries",
					"entries": [
						"Githyanki tend toward lawful evil. They are aggressive and arrogant, and they remain the faithful servants of their lich-queen, Vlaakith. Renegade githyanki tend toward chaos."
					]
				},
				{
					"name": "Decadent Mastery",
					"entries": [
						"You learn one language of your choice, and you are proficient with one skill or {@book tool|phb|5|tools} of your choice. In the timeless city of Tu'narath, githyanki have bountiful time to master odd bits of knowledge."
					],
					"type": "entries"
				},
				{
					"name": "Martial Prodigy",
					"entries": [
						"You are proficient with light and medium armor and with {@item shortsword|phb|shortswords}, {@item longsword|phb|longswords}, and {@item greatsword|phb|greatswords}."
					],
					"type": "entries"
				},
				{
					"name": "Githyanki Psionics",
					"entries": [
						"You know the {@spell mage hand} cantrip, and the hand is {@condition invisible} when you cast the cantrip with this trait.",
						"When you reach 3rd level, you can cast {@spell jump} once with this trait, and you regain the ability to do so when you finish a long rest. When you reach 5th level, you can cast the {@spell misty step} spell once with this trait, and you regain the ability to do so when you finish a long rest.",
						"Intelligence is your spellcasting ability for these spells. When you cast them with this trait, they don't require components."
					],
					"type": "entries"
				}
			],
			"hasFluff": true,
			"hasFluffImages": true
		},
		{
			"name": "Githzerai",
			"source": "MTF",
			"raceName": "Gith",
			"raceSource": "MTF",
			"page": 96,
			"reprintedAs": [
				"Githzerai|MPMM"
			],
			"ability": [
				{
					"wis": 2
				}
			],
			"heightAndWeight": {
				"baseHeight": 59,
				"heightMod": "2d12",
				"baseWeight": 90,
				"weightMod": "1d4"
			},
			"additionalSpells": [
				{
					"innate": {
						"3": {
							"daily": {
								"1": [
									"shield"
								]
							}
						},
						"5": {
							"daily": {
								"1": [
									"detect thoughts"
								]
							}
						}
					},
					"ability": "wis",
					"known": {
						"1": [
							"mage hand#c"
						]
					}
				}
			],
			"entries": [
				{
					"name": "Alignment",
					"type": "entries",
					"entries": [
						"Githzerai tend toward lawful neutral. Their rigorous training in psychic abilities requires an implacable mental discipline."
					]
				},
				{
					"name": "Mental Discipline",
					"entries": [
						"You have advantage on saving throws against the {@condition charmed} and {@condition frightened} conditions. Under the tutelage of monastic masters, githzerai learn to govern their own minds."
					],
					"type": "entries"
				},
				{
					"name": "Githzerai Psionics",
					"entries": [
						"You know the {@spell mage hand} cantrip, and the hand is {@condition invisible} when you cast the cantrip with this trait.",
						"When you reach 3rd level, you can cast {@spell shield} once with this trait, and you regain the ability to do so when you finish a long rest. When you reach 5th level, you can cast the {@spell detect thoughts} spell once with this trait, and you regain the ability to do so when you finish a long rest.",
						"Wisdom is your spellcasting ability for these spells. When you cast them with this trait, they don't require components."
					],
					"type": "entries"
				}
			],
			"hasFluff": true
		},
		{
			"name": "Githyanki",
			"source": "UAEladrinAndGith",
			"raceName": "Gith",
			"raceSource": "UAEladrinAndGith",
			"page": 2,
			"reprintedAs": [
				"Gith (Githyanki)|MTF"
			],
			"ability": [
				{
					"str": 2
				}
			],
			"traitTags": [
				"Skill Proficiency",
				"Tool Proficiency"
			],
			"armorProficiencies": [
				{
					"light": true,
					"medium": true
				}
			],
			"skillToolLanguageProficiencies": [
				{
					"choose": [
						{
							"from": [
								"anySkill",
								"anyTool"
							]
						}
					]
				}
			],
			"additionalSpells": [
				{
					"innate": {
						"3": {
							"daily": {
								"1": [
									"jump"
								]
							}
						},
						"5": {
							"daily": {
								"1": [
									"misty step"
								]
							}
						}
					},
					"ability": "int",
					"known": {
						"1": [
							"mage hand#c"
						]
					}
				}
			],
			"entries": [
				{
					"name": "Alignment",
					"type": "entries",
					"entries": [
						"Githyanki tend toward lawful evil. They are self-centered, violent, and arrogant, yet they remain the faithful servants of their lich-queen, Vlaakith. Renegade githyanki tend toward chaos as they have forsaken her will."
					]
				},
				{
					"name": "Decadent Mastery",
					"entries": [
						"You learn one language of your choice, and you are proficient with one skill or {@book tool|phb|5|tools} of your choice. In the timeless city of Tu'narath, githyanki have bountiful time to master odd bits of knowledge."
					],
					"type": "entries"
				},
				{
					"name": "Martial Prodigy",
					"entries": [
						"You are proficient with light and medium armor. Your people are ever ready for war."
					],
					"type": "entries"
				},
				{
					"name": "Githyanki Psionics",
					"entries": [
						"You know the {@spell mage hand} cantrip. When you reach 3rd level, you can cast {@spell jump} once with this trait, and you regain the ability to do so when you finish a long rest. When you reach 5th level, you can cast the {@spell misty step} spell once with this trait, and you regain the ability to do so when you finish a long rest.",
						"Intelligence is your spellcasting ability for these spells. You can cast all of them without components."
					],
					"type": "entries"
				}
			]
		},
		{
			"name": "Githzerai",
			"source": "UAEladrinAndGith",
			"raceName": "Gith",
			"raceSource": "UAEladrinAndGith",
			"page": 3,
			"reprintedAs": [
				"Gith (Githzerai)|MTF"
			],
			"ability": [
				{
					"wis": 2
				}
			],
			"traitTags": [
				"Natural Armor"
			],
			"additionalSpells": [
				{
					"innate": {
						"3": {
							"daily": {
								"1": [
									"shield"
								]
							}
						},
						"5": {
							"daily": {
								"1": [
									"detect thoughts"
								]
							}
						}
					},
					"ability": "wis",
					"known": {
						"1": [
							"mage hand#c"
						]
					}
				}
			],
			"entries": [
				{
					"name": "Alignment",
					"type": "entries",
					"entries": [
						"Githzerai tend toward lawful neutral. Their rigorous training in psychic abilities requires an implacable mental discipline."
					]
				},
				{
					"name": "Monastic Training",
					"entries": [
						"You gain a +1 bonus to AC while you aren't wearing medium or heavy armor and aren't using a shield. All githzerai receive basic training from monks, and the monks among them are unmatched in their defensive abilities."
					],
					"type": "entries"
				},
				{
					"name": "Githzerai Psionics",
					"entries": [
						"You know the {@spell mage hand} cantrip. When you reach 3rd level, you can cast {@spell shield} once with this trait, and you regain the ability to do so when you finish a long rest. When you reach 5th level, you can cast the {@spell detect thoughts} spell once with this trait, and you regain the ability to do so when you finish a long rest.",
						"Wisdom is your spellcasting ability for these spells. You can cast all of them without components."
					],
					"type": "entries"
				}
			]
		},
		{
			"name": "Deep",
			"source": "MTF",
			"raceName": "Gnome",
			"raceSource": "PHB",
			"page": 113,
			"reprintedAs": [
				"Deep Gnome|MPMM"
			],
			"ability": [
				{
					"dex": 1
				}
			],
			"age": {
				"mature": 25,
				"max": 250
			},
			"darkvision": 120,
			"languageProficiencies": [
				{
					"common": true,
					"gnomish": true,
					"undercommon": true
				}
			],
			"entries": [
				{
					"name": "Age",
					"type": "entries",
					"entries": [
						"Deep gnomes are short-lived for gnomes. They mature at the same rate humans do and are considered full-grown adults by 25. They live 200 to 250 years, although hard toil and the dangers of the Underdark often claim them before their time."
					],
					"data": {
						"overwrite": "Age"
					}
				},
				{
					"type": "entries",
					"name": "Size",
					"entries": [
						"Unlike other gnomes, svirfneblin tend to weigh 80 to 120 pounds. Your size is Small."
					],
					"data": {
						"overwrite": "Size"
					}
				},
				{
					"name": "Alignment",
					"type": "entries",
					"entries": [
						"Svirfneblin believe that survival depends on avoiding entanglements with other creatures and not making enemies, so they favor neutral alignments. They rarely wish others ill, and they are unlikely to take risks on behalf of others, except those dearest to them."
					],
					"data": {
						"overwrite": "Alignment"
					}
				},
				{
					"name": "Superior Darkvision",
					"entries": [
						"Accustomed to life underground, you have superior vision in dark and dim conditions. You can see in dim light within 120 feet of you as if it were bright light, and in darkness as if it were dim light. You can't discern color in darkness, only shades of gray."
					],
					"data": {
						"overwrite": "Darkvision"
					},
					"type": "entries"
				},
				{
					"name": "Stone Camouflage",
					"entries": [
						"You have advantage on Dexterity ({@skill Stealth}) checks to hide in rocky terrain."
					],
					"type": "entries"
				},
				{
					"name": "Languages",
					"entries": [
						"You can speak, read, and write Common, Gnomish, and Undercommon."
					],
					"data": {
						"overwrite": "Languages"
					},
					"type": "entries"
				}
			],
			"overwrite": {
				"languageProficiencies": true
			}
		},
		{
			"name": "Deep/Svirfneblin",
			"source": "SCAG",
			"raceName": "Gnome",
			"raceSource": "PHB",
			"page": 115,
			"otherSources": [
				{
					"source": "EEPC",
					"page": 5
				}
			],
			"reprintedAs": [
				"Deep Gnome|MPMM"
			],
			"ability": [
				{
					"dex": 1
				}
			],
			"age": {
				"mature": 25,
				"max": 250
			},
			"darkvision": 120,
			"languageProficiencies": [
				{
					"common": true,
					"gnomish": true,
					"undercommon": true
				}
			],
			"entries": [
				{
					"name": "Age",
					"type": "entries",
					"entries": [
						"Deep gnomes are short-lived for gnomes. They mature at the same rate humans do and are considered full-grown adults by 25. They live 200 to 250 years, although hard toil and the dangers of the Underdark often claim them before their time."
					],
					"data": {
						"overwrite": "Age"
					}
				},
				{
					"name": "Alignment",
					"type": "entries",
					"entries": [
						"Svirfneblin believe that survival depends on avoiding entanglements with other creatures and not making enemies, so they favor neutral alignments. They rarely wish others ill, and they are unlikely to take risks on behalf of others."
					],
					"data": {
						"overwrite": "Alignment"
					}
				},
				{
					"type": "entries",
					"name": "Size",
					"entries": [
						"A typical svirfneblin stands about 3 to 3½ feet tall and weighs 80 to 120 pounds. Your size is Small."
					],
					"data": {
						"overwrite": "Size"
					}
				},
				{
					"name": "Superior Darkvision",
					"entries": [
						"Accustomed to life underground, you have superior vision in dark and dim conditions. You can see in dim light within 120 feet of you as if it were bright light, and in darkness as if it were dim light. You can't discern color in darkness, only shades of gray."
					],
					"data": {
						"overwrite": "Darkvision"
					},
					"type": "entries"
				},
				{
					"name": "Stone Camouflage",
					"entries": [
						"You have advantage on Dexterity ({@skill Stealth}) checks to hide in rocky terrain."
					],
					"type": "entries"
				},
				{
					"name": "Languages",
					"entries": [
						"You can speak, read, and write Common, Gnomish, and Undercommon. The svirfneblin dialect is more guttural than surface Gnomish, and most svirfneblin know only a little bit of Common, but those who deal with outsiders (and that includes you as an adventurer) pick up enough Common to get by in other lands."
					],
					"data": {
						"overwrite": "Languages"
					},
					"type": "entries"
				}
			],
			"overwrite": {
				"languageProficiencies": true
			},
			"hasFluff": true
		},
		{
			"name": "Forest",
			"source": "PHB",
			"raceName": "Gnome",
			"raceSource": "PHB",
			"page": 37,
			"ability": [
				{
					"dex": 1
				}
			],
			"additionalSpells": [
				{
					"ability": "int",
					"known": {
						"1": [
							"minor illusion#c"
						]
					}
				}
			],
			"entries": [
				{
					"name": "Natural Illusionist",
					"entries": [
						"You know the {@spell minor illusion} cantrip. Intelligence is your spellcasting ability for it."
					],
					"type": "entries"
				},
				{
					"name": "Speak with Small Beasts",
					"entries": [
						"Through sounds and gestures, you can communicate simple ideas with Small or smaller beasts. Forest gnomes love animals and often keep squirrels, badgers, rabbits, moles, woodpeckers, and other creatures as beloved pets."
					],
					"type": "entries"
				}
			],
			"hasFluff": true,
			"hasFluffImages": true
		},
		{
			"name": "Mark of Scribing",
			"source": "ERLW",
			"raceName": "Gnome",
			"raceSource": "PHB",
			"page": 47,
			"otherSources": [
				{
					"source": "UAWGE",
					"page": 103
				}
			],
			"ability": [
				{
					"cha": 1
				}
			],
			"traitTags": [
				"Dragonmark",
				"Skill Bonus Dice",
				"Tool Bonus Dice"
			],
			"additionalSpells": [
				{
					"innate": {
						"1": {
							"rest": {
								"1": [
									"comprehend languages"
								]
							}
						},
						"3": {
							"daily": {
								"1": [
									"magic mouth"
								]
							}
						}
					},
					"expanded": {
						"s1": [
							"comprehend languages",
							"illusory script"
						],
						"s2": [
							"animal messenger",
							"silence"
						],
						"s3": [
							"sending",
							"tongues"
						],
						"s4": [
							"arcane eye",
							"confusion"
						],
						"s5": [
							"dream"
						]
					},
					"ability": "int",
					"known": {
						"1": [
							"message#c"
						]
					}
				}
			],
			"entries": [
				{
					"type": "entries",
					"name": "Gifted Scribe",
					"entries": [
						"When you make an Intelligence ({@skill History}) check or an ability check using {@item calligrapher's supplies|PHB}, you can roll a {@dice d4} and add the number rolled to the ability check."
					]
				},
				{
					"type": "entries",
					"name": "Scribe's Insight",
					"entries": [
						"You know the {@spell message} cantrip. You can also cast {@spell comprehend languages} once with this trait, and you regain the ability to cast it when you finish a short or long rest. Starting at 3rd level, you can cast the {@spell magic mouth} spell with this trait, and you regain the ability to cast it when you finish a long rest. Intelligence is your spellcasting ability for these spells."
					]
				},
				{
					"type": "entries",
					"name": "Spells of the Mark",
					"entries": [
						"If you have the Spellcasting or the Pact Magic class feature, the spells on the Mark of Scribing Spells table are added to the spell list of your spellcasting class.",
						{
							"type": "table",
							"caption": "Mark of Scribing Spells",
							"colLabels": [
								"Spell Level",
								"Spells"
							],
							"colStyles": [
								"col-2 text-center",
								"col-10"
							],
							"rows": [
								[
									"1st",
									"{@spell comprehend languages}, {@spell illusory script}"
								],
								[
									"2nd",
									"{@spell animal messenger}, {@spell silence}"
								],
								[
									"3rd",
									"{@spell sending}, {@spell tongues}"
								],
								[
									"4th",
									"{@spell arcane eye}, {@spell confusion}"
								],
								[
									"5th",
									"{@spell dream}"
								]
							]
						}
					]
				}
			]
		},
		{
			"name": "Rock",
			"source": "PHB",
			"raceName": "Gnome",
			"raceSource": "PHB",
			"page": 37,
			"srd": true,
			"ability": [
				{
					"con": 1
				}
			],
			"traitTags": [
				"Tool Proficiency"
			],
			"entries": [
				{
					"name": "Artificer's Lore",
					"entries": [
						"Whenever you make an Intelligence ({@skill History}) check related to magic items, alchemical objects, or technological devices, you can add twice your proficiency bonus, instead of any proficiency bonus you normally apply."
					],
					"type": "entries"
				},
				{
					"name": "Tinker",
					"entries": [
						"You have proficiency with artisan's tools ({@item tinker's tools|phb}). Using those tools, you can spend 1 hour and 10 gp worth of materials to construct a Tiny clockwork device (AC 5, 1 hp). The device ceases to function after 24 hours (unless you spend 1 hour repairing it to keep the device functioning), or when you use your action to dismantle it; at that time, you can reclaim the materials used to create it. You can have up to three such devices active at a time.",
						"When you create a device, choose one of the following options:",
						{
							"type": "entries",
							"name": "Clockwork Toy",
							"entries": [
								"This toy is a clockwork animal, monster, or person, such as a frog, mouse, bird, dragon, or soldier. When placed on the ground, the toy moves 5 feet across the ground on each of your turns in a random direction. It makes noises as appropriate to the creature it represents."
							]
						},
						{
							"type": "entries",
							"name": "Fire Starter",
							"entries": [
								"The device produces a miniature flame, which you can use to light a candle, torch, or campfire. Using the device requires your action."
							]
						},
						{
							"type": "entries",
							"name": "Music Box",
							"entries": [
								"When opened, this music box plays a single song at a moderate volume. The box stops playing when it reaches the song's end or when it is closed."
							]
						}
					],
					"type": "entries"
				}
			],
			"hasFluff": true,
			"hasFluffImages": true
		},
		{
			"name": "Grotag Tribe",
			"source": "PSZ",
			"raceName": "Goblin (Zendikar)",
			"raceSource": "PSZ",
			"page": 17,
			"skillProficiencies": [
				{
					"animal handling": true
				}
			],
			"entries": [
				{
					"name": "Grotag Tamer",
					"entries": [
						"You have proficiency in the {@skill Animal Handling} skill."
					],
					"type": "entries"
				}
			],
			"hasFluff": true,
			"hasFluffImages": true
		},
		{
			"name": "Lavastep Tribe",
			"source": "PSZ",
			"raceName": "Goblin (Zendikar)",
			"raceSource": "PSZ",
			"page": 17,
			"entries": [
				{
					"name": "Lavastep Grit",
					"entries": [
						"You have advantage on Dexterity ({@skill Stealth}) checks made to hide in rocky or subterranean environments."
					],
					"type": "entries"
				}
			],
			"hasFluff": true,
			"hasFluffImages": true
		},
		{
			"name": "Tuktuk Tribe",
			"source": "PSZ",
			"raceName": "Goblin (Zendikar)",
			"raceSource": "PSZ",
			"page": 17,
			"traitTags": [
				"Tool Proficiency"
			],
			"entries": [
				{
					"name": "Tuktuk Cunning",
					"entries": [
						"You have proficiency with {@item thieves' tools|phb}."
					],
					"type": "entries"
				}
			],
			"hasFluff": true,
			"hasFluffImages": true
		},
		{
			"source": "PHB",
			"raceName": "Half-Elf",
			"raceSource": "PHB",
			"page": 38,
			"srd": true,
			"hasFluff": true,
			"hasFluffImages": true
		},
		{
			"name": "Variant; Aquatic Elf Descent",
			"source": "SCAG",
			"raceName": "Half-Elf",
			"raceSource": "PHB",
			"page": 116,
			"speed": {
				"walk": 30,
				"swim": 30
			},
			"skillProficiencies": [
				{
					"any": 2
				}
			],
			"entries": [
				{
					"type": "inset",
					"name": "Variant Feature (Choose 1)",
					"entries": [
						{
							"name": "Skill Versatility",
							"entries": [
								"You gain proficiency in two skills of your choice."
							],
							"type": "entries"
						},
						{
							"name": "Swim",
							"entries": [
								"You gain a swimming speed of 30 ft."
							],
							"type": "entries"
						}
					],
					"data": {
						"overwrite": "Skill Versatility"
					}
				}
			],
			"overwrite": {
				"skillProficiencies": true
			},
			"_versions": [
				{
					"name": "Variant; Aquatic Elf Descent; Skill Versatility",
					"source": "SCAG",
					"_mod": {
						"entries": {
							"mode": "replaceArr",
							"replace": "Variant Feature (Choose 1)",
							"items": {
								"name": "Variant Feature; Skill Versatility",
								"type": "entries",
								"entries": [
									"You gain proficiency in two skills of your choice."
								]
							}
						}
					},
					"speed": 30
				},
				{
					"name": "Variant; Aquatic Elf Descent; Swim Speed",
					"source": "SCAG",
					"_mod": {
						"entries": {
							"mode": "replaceArr",
							"replace": "Variant Feature (Choose 1)",
							"items": {
								"name": "Variant Feature; Swim Speed",
								"type": "entries",
								"entries": [
									"You gain a swimming speed of 30 ft."
								]
							}
						}
					},
					"skillProficiencies": null
				}
			]
		},
		{
			"name": "Variant; Drow Descent",
			"source": "SCAG",
			"raceName": "Half-Elf",
			"raceSource": "PHB",
			"page": 116,
			"skillProficiencies": [
				{
					"any": 2
				}
			],
			"additionalSpells": [
				{
					"innate": {
						"3": {
							"daily": {
								"1": [
									"faerie fire"
								]
							}
						},
						"5": {
							"daily": {
								"1": [
									"darkness"
								]
							}
						}
					},
					"ability": "cha",
					"known": {
						"1": [
							"dancing lights#c"
						]
					}
				}
			],
			"entries": [
				{
					"type": "inset",
					"name": "Variant Feature (Choose 1)",
					"entries": [
						{
							"name": "Skill Versatility",
							"entries": [
								"You gain proficiency in two skills of your choice."
							],
							"type": "entries"
						},
						{
							"name": "Drow Magic",
							"entries": [
								"You know the {@spell dancing lights} cantrip. When you reach 3rd level, you can cast the {@spell faerie fire} spell once per day; you must finish a long rest in order to cast the spell again using this trait. When you reach 5th level, you can also cast the {@spell darkness} spell once per day; you must finish a long rest in order to cast the spell again using this trait. Charisma is your spellcasting ability for these spells."
							],
							"type": "entries"
						}
					],
					"data": {
						"overwrite": "Skill Versatility"
					}
				}
			],
			"overwrite": {
				"skillProficiencies": true
			},
			"_versions": [
				{
					"name": "Variant; Drow Descent; Drow Magic",
					"source": "SCAG",
					"_mod": {
						"entries": {
							"mode": "replaceArr",
							"replace": "Variant Feature (Choose 1)",
							"items": {
								"name": "Variant Feature; Drow Magic",
								"type": "entries",
								"entries": [
									"You know the {@spell dancing lights} cantrip. When you reach 3rd level, you can cast the {@spell faerie fire} spell once per day; you must finish a long rest in order to cast the spell again using this trait. When you reach 5th level, you can also cast the {@spell darkness} spell once per day; you must finish a long rest in order to cast the spell again using this trait. Charisma is your spellcasting ability for these spells."
								]
							}
						}
					},
					"skillProficiencies": null
				},
				{
					"name": "Variant; Drow Descent; Skill Versatility",
					"source": "SCAG",
					"_mod": {
						"entries": {
							"mode": "replaceArr",
							"replace": "Variant Feature (Choose 1)",
							"items": {
								"name": "Variant Feature; Skill Versatility",
								"type": "entries",
								"entries": [
									"You gain proficiency in two skills of your choice."
								]
							}
						}
					},
					"additionalSpells": null
				}
			]
		},
		{
			"name": "Variant; Mark of Detection",
			"source": "ERLW",
			"raceName": "Half-Elf",
			"raceSource": "PHB",
			"page": 40,
			"otherSources": [
				{
					"source": "UAWGE",
					"page": 96
				}
			],
			"ability": [
				{
					"wis": 2,
					"choose": {
						"from": [
							"str",
							"dex",
							"con",
							"int",
							"cha"
						],
						"count": 1
					}
				}
			],
			"traitTags": [
				"Dragonmark",
				"Skill Bonus Dice"
			],
			"skillProficiencies": null,
			"additionalSpells": [
				{
					"innate": {
						"1": [
							"detect magic",
							"detect poison and disease"
						],
						"3": {
							"daily": {
								"1": [
									"see invisibility"
								]
							}
						}
					},
					"expanded": {
						"s1": [
							"detect evil and good",
							"detect poison and disease"
						],
						"s2": [
							"detect thoughts",
							"find traps"
						],
						"s3": [
							"clairvoyance",
							"nondetection"
						],
						"s4": [
							"arcane eye",
							"divination"
						],
						"s5": [
							"legend lore"
						]
					},
					"ability": "int"
				}
			],
			"entries": [
				{
					"type": "entries",
					"name": "Deductive Intuition",
					"entries": [
						"When you make an Intelligence ({@skill Investigation}) or a Wisdom ({@skill Insight}) check, you can roll a {@dice d4} and add the number rolled to the ability check."
					],
					"data": {
						"overwrite": "Skill Versatility"
					}
				},
				{
					"type": "entries",
					"name": "Magical Detection",
					"entries": [
						"You can cast the {@spell detect magic} and {@spell detect poison and disease} spells with this trait. Starting at 3rd level, you can also cast the {@spell see invisibility} spell with it. Once you cast any of these spells with this trait, you can't cast that spell with it again until you finish a long rest. Wisdom is your spellcasting ability for these spells, and you don't require material components for them."
					]
				},
				{
					"type": "entries",
					"name": "Spells of the Mark",
					"entries": [
						"If you have the Spellcasting or the Pact Magic class feature, the spells on the Mark of Detection Spells table are added to the spell list of your spellcasting class.",
						{
							"type": "table",
							"caption": "Mark of Detection Spells",
							"colLabels": [
								"Spell Level",
								"Spells"
							],
							"colStyles": [
								"col-2 text-center",
								"col-10"
							],
							"rows": [
								[
									"1st",
									"{@spell detect evil and good}, {@spell detect poison and disease}"
								],
								[
									"2nd",
									"{@spell detect thoughts}, {@spell find traps}"
								],
								[
									"3rd",
									"{@spell clairvoyance}, {@spell nondetection}"
								],
								[
									"4th",
									"{@spell arcane eye}, {@spell divination}"
								],
								[
									"5th",
									"{@spell legend lore}"
								]
							]
						}
					]
				}
			],
			"overwrite": {
				"ability": true
			}
		},
		{
			"name": "Variant; Mark of Storm",
			"source": "ERLW",
			"raceName": "Half-Elf",
			"raceSource": "PHB",
			"page": 50,
			"otherSources": [
				{
					"source": "UAWGE",
					"page": 106
				}
			],
			"ability": [
				{
					"cha": 2,
					"dex": 1
				}
			],
			"traitTags": [
				"Dragonmark",
				"Skill Bonus Dice",
				"Tool Bonus Dice"
			],
			"skillProficiencies": null,
			"resist": [
				"lightning"
			],
			"additionalSpells": [
				{
					"expanded": {
						"s1": [
							"feather fall",
							"fog cloud"
						],
						"s2": [
							"gust of wind",
							"levitate"
						],
						"s3": [
							"sleet storm",
							"wind wall"
						],
						"s4": [
							"conjure minor elementals",
							"control water"
						],
						"s5": [
							"conjure elemental"
						]
					},
					"ability": "cha",
					"known": {
						"1": [
							"gust|xge#c"
						]
					}
				}
			],
			"entries": [
				{
					"type": "entries",
					"name": "Windwright's Intuition",
					"entries": [
						"When you make a Dexterity ({@skill Acrobatics}) check or any ability check involving {@item navigator's tools|PHB}, you can roll a {@dice d4} and add the number rolled to the ability check."
					],
					"data": {
						"overwrite": "Skill Versatility"
					}
				},
				{
					"type": "entries",
					"name": "Storm's Boon",
					"entries": [
						"You have resistance to lightning damage."
					]
				},
				{
					"type": "entries",
					"name": "Headwinds",
					"entries": [
						"You know the {@spell gust|XGE} cantrip. Starting at 3rd level, you can cast the {@spell gust of wind} spell once with this trait, and you regain the ability to cast it when you finish a long rest. Charisma is your spellcasting ability for these spells."
					]
				},
				{
					"type": "entries",
					"name": "Spells of the Mark",
					"entries": [
						"If you have the Spellcasting or the Pact Magic class feature, the spells on the Mark of Storm Spells table are added to the spell list of your spellcasting class.",
						{
							"type": "table",
							"caption": "Mark of Storm Spells",
							"colLabels": [
								"Spell Level",
								"Spells"
							],
							"colStyles": [
								"col-2 text-center",
								"col-10"
							],
							"rows": [
								[
									"1st",
									"{@spell feather fall}, {@spell fog cloud}"
								],
								[
									"2nd",
									"{@spell gust of wind}, {@spell levitate}"
								],
								[
									"3rd",
									"{@spell sleet storm}, {@spell wind wall}"
								],
								[
									"4th",
									"{@spell conjure minor elementals}, {@spell control water}"
								],
								[
									"5th",
									"{@spell conjure elemental}"
								]
							]
						}
					]
				}
			],
			"overwrite": {
				"ability": true
			}
		},
		{
			"name": "Variant; Moon Elf or Sun Elf Descent",
			"source": "SCAG",
			"raceName": "Half-Elf",
			"raceSource": "PHB",
			"page": 116,
			"skillProficiencies": [
				{
					"any": 2
				}
			],
			"weaponProficiencies": [
				{
					"longsword|phb": true,
					"shortsword|phb": true,
					"shortbow|phb": true,
					"longbow|phb": true
				}
			],
			"additionalSpells": [
				{
					"ability": "int",
					"known": {
						"1": {
							"_": [
								{
									"choose": "level=0|class=Wizard"
								}
							]
						}
					}
				}
			],
			"entries": [
				{
					"type": "inset",
					"name": "Variant Feature (Choose 1)",
					"entries": [
						{
							"name": "Skill Versatility",
							"entries": [
								"You gain proficiency in two skills of your choice."
							],
							"type": "entries"
						},
						{
							"name": "Elf Weapon Training",
							"entries": [
								"You have proficiency with the {@item longsword|phb}, {@item shortsword|phb}, {@item shortbow|phb}, and {@item longbow|phb}."
							],
							"type": "entries"
						},
						{
							"name": "Cantrip",
							"entries": [
								"You know one cantrip of your choice from the {@filter wizard spell list|spells|class=wizard|level=0}. Intelligence is your spellcasting ability for it."
							],
							"type": "entries"
						}
					],
					"data": {
						"overwrite": "Skill Versatility"
					}
				}
			],
			"overwrite": {
				"skillProficiencies": true
			},
			"_versions": [
				{
					"name": "Variant; Moon Elf or Sun Elf Descent; Cantrip",
					"source": "SCAG",
					"_mod": {
						"entries": {
							"mode": "replaceArr",
							"replace": "Variant Feature (Choose 1)",
							"items": {
								"name": "Variant Feature; Cantrip",
								"type": "entries",
								"entries": [
									"You know one cantrip of your choice from the {@filter wizard spell list|spells|class=wizard|level=0}. Intelligence is your spellcasting ability for it."
								]
							}
						}
					},
					"skillProficiencies": null,
					"weaponProficiencies": null
				},
				{
					"name": "Variant; Moon Elf or Sun Elf Descent; Elf Weapon Training",
					"source": "SCAG",
					"_mod": {
						"entries": {
							"mode": "replaceArr",
							"replace": "Variant Feature (Choose 1)",
							"items": {
								"name": "Variant Feature; Elf Weapon Training",
								"type": "entries",
								"entries": [
									"You have proficiency with the {@item longsword|phb}, {@item shortsword|phb}, {@item shortbow|phb}, and {@item longbow|phb}."
								]
							}
						}
					},
					"skillProficiencies": null,
					"additionalSpells": null
				},
				{
					"name": "Variant; Moon Elf or Sun Elf Descent; Skill Versatility",
					"source": "SCAG",
					"_mod": {
						"entries": {
							"mode": "replaceArr",
							"replace": "Variant Feature (Choose 1)",
							"items": {
								"name": "Variant Feature; Skill Versatility",
								"type": "entries",
								"entries": [
									"You gain proficiency in two skills of your choice."
								]
							}
						}
					},
					"weaponProficiencies": null,
					"additionalSpells": null
				}
			]
		},
		{
			"name": "Variant; Wood Elf Descent",
			"source": "SCAG",
			"raceName": "Half-Elf",
			"raceSource": "PHB",
			"page": 116,
			"skillProficiencies": [
				{
					"any": 2
				}
			],
			"weaponProficiencies": [
				{
					"longsword|phb": true,
					"shortsword|phb": true,
					"shortbow|phb": true,
					"longbow|phb": true
				}
			],
			"entries": [
				{
					"type": "inset",
					"name": "Variant Feature (Choose 1)",
					"entries": [
						{
							"name": "Skill Versatility",
							"entries": [
								"You gain proficiency in two skills of your choice."
							],
							"type": "entries"
						},
						{
							"name": "Elf Weapon Training",
							"entries": [
								"You have proficiency with the {@item longsword|phb}, {@item shortsword|phb}, {@item shortbow|phb}, and {@item longbow|phb}."
							],
							"type": "entries"
						},
						{
							"name": "Fleet of Foot",
							"entries": [
								"Your base walking speed increases to 35 feet."
							],
							"type": "entries"
						},
						{
							"name": "Mask of the Wild",
							"entries": [
								"You can attempt to hide even when you are only lightly obscured by foliage, heavy rain, falling snow, mist, and other natural phenomena."
							],
							"type": "entries"
						}
					],
					"data": {
						"overwrite": "Skill Versatility"
					}
				}
			],
			"overwrite": {
				"skillProficiencies": true
			},
			"_versions": [
				{
					"name": "Variant; Wood Elf Descent; Elf Weapon Training",
					"source": "SCAG",
					"_mod": {
						"entries": {
							"mode": "replaceArr",
							"replace": "Variant Feature (Choose 1)",
							"items": {
								"name": "Variant Feature; Elf Weapon Training",
								"type": "entries",
								"entries": [
									"You have proficiency with the {@item longsword|phb}, {@item shortsword|phb}, {@item shortbow|phb}, and {@item longbow|phb}."
								]
							}
						}
					},
					"skillProficiencies": null
				},
				{
					"name": "Variant; Wood Elf Descent; Fleet of Foot",
					"source": "SCAG",
					"_mod": {
						"entries": {
							"mode": "replaceArr",
							"replace": "Variant Feature (Choose 1)",
							"items": {
								"name": "Variant Feature; Fleet of Foot",
								"type": "entries",
								"entries": [
									"Your base walking speed increases to 35 feet."
								]
							}
						}
					},
					"speed": 35,
					"skillProficiencies": null,
					"weaponProficiencies": null
				},
				{
					"name": "Variant; Wood Elf Descent; Mask of the Wild",
					"source": "SCAG",
					"_mod": {
						"entries": {
							"mode": "replaceArr",
							"replace": "Variant Feature (Choose 1)",
							"items": {
								"name": "Variant Feature; Mask of the Wild",
								"type": "entries",
								"entries": [
									"You can attempt to hide even when you are only lightly obscured by foliage, heavy rain, falling snow, mist, and other natural phenomena."
								]
							}
						}
					},
					"skillProficiencies": null,
					"weaponProficiencies": null
				},
				{
					"name": "Variant; Wood Elf Descent; Skill Versatility",
					"source": "SCAG",
					"_mod": {
						"entries": {
							"mode": "replaceArr",
							"replace": "Variant Feature (Choose 1)",
							"items": {
								"name": "Variant Feature; Skill Versatility",
								"type": "entries",
								"entries": [
									"You gain proficiency in two skills of your choice."
								]
							}
						}
					},
					"weaponProficiencies": null
				}
			]
		},
		{
			"source": "PHB",
			"raceName": "Half-Orc",
			"raceSource": "PHB",
			"page": 40,
			"srd": true,
			"hasFluff": true,
			"hasFluffImages": true
		},
		{
			"name": "Variant; Mark of Finding",
			"source": "ERLW",
			"raceName": "Half-Orc",
			"raceSource": "PHB",
			"page": 41,
			"otherSources": [
				{
					"source": "UAWGE",
					"page": 98
				}
			],
			"traitTags": [
				"Dragonmark",
				"Skill Bonus Dice"
			],
			"languageProficiencies": [
				{
					"common": true,
					"goblin": true
				}
			],
			"soundClip": {
				"type": "internal",
				"path": "races/half-orc.mp3"
			},
			"additionalSpells": [
				{
					"innate": {
						"1": [
							"hunter's mark"
						],
						"3": {
							"daily": {
								"1": [
									"locate object"
								]
							}
						}
					},
					"expanded": {
						"s1": [
							"faerie fire",
							"longstrider"
						],
						"s2": [
							"locate animals or plants",
							"locate object"
						],
						"s3": [
							"clairvoyance",
							"speak with plants"
						],
						"s4": [
							"divination",
							"locate creature"
						],
						"s5": [
							"commune with nature"
						]
					},
					"ability": "wis"
				}
			],
			"entries": [
				{
					"type": "entries",
					"name": "Darkvision",
					"entries": [
						"You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. You can't discern color in darkness, only shades of gray."
					],
					"data": {
						"overwrite": "Darkvision"
					}
				},
				{
					"type": "entries",
					"name": "Hunter's Intuition",
					"entries": [
						"When you make a Wisdom ({@skill Perception}) or Wisdom ({@skill Survival}) check, you can roll a {@dice d4} and add the number rolled to the ability check."
					],
					"data": {
						"overwrite": "Menacing"
					}
				},
				{
					"type": "entries",
					"name": "Finder's Magic",
					"entries": [
						"You can cast the {@spell hunter's mark} spell with this trait. Starting at 3rd level, you can also cast the {@spell locate object} spell with it. Once you cast either spell with this trait, you can't cast that spell with it again until you finish a long rest. Wisdom is your spellcasting ability for these spells."
					],
					"data": {
						"overwrite": "Relentless Endurance"
					}
				},
				{
					"type": "entries",
					"name": "Languages",
					"entries": [
						"You can speak, read, and write Common and Goblin."
					],
					"data": {
						"overwrite": "Languages"
					}
				},
				{
					"type": "entries",
					"name": "Spells of the Mark",
					"entries": [
						"If you have the Spellcasting or the Pact Magic class feature, the spells on the Mark of Finding Spells table are added to the spell list of your spellcasting class.",
						{
							"type": "table",
							"caption": "Mark of Finding Spells",
							"colLabels": [
								"Spell Level",
								"Spells"
							],
							"colStyles": [
								"col-2 text-center",
								"col-10"
							],
							"rows": [
								[
									"1st",
									"{@spell faerie fire}, {@spell longstrider}"
								],
								[
									"2nd",
									"{@spell locate animals or plants}, {@spell locate object}"
								],
								[
									"3rd",
									"{@spell clairvoyance}, {@spell speak with plants}"
								],
								[
									"4th",
									"{@spell divination}, {@spell locate creature}"
								],
								[
									"5th",
									"{@spell commune with nature}"
								]
							]
						}
					],
					"data": {
						"overwrite": "Savage Attacks"
					}
				}
			]
		},
		{
			"name": "Ghostwise",
			"source": "SCAG",
			"raceName": "Halfling",
			"raceSource": "PHB",
			"page": 110,
			"ability": [
				{
					"wis": 1
				}
			],
			"entries": [
				{
					"name": "Silent Speech",
					"entries": [
						"You can speak telepathically to any creature within 30 feet of you. The creature understands you only if the two of you share a language. You can speak telepathically in this way to one creature at a time."
					],
					"type": "entries"
				}
			],
			"hasFluff": true,
			"hasFluffImages": true
		},
		{
			"name": "Lightfoot",
			"source": "PHB",
			"raceName": "Halfling",
			"raceSource": "PHB",
			"page": 28,
			"srd": true,
			"basicRules": true,
			"ability": [
				{
					"cha": 1
				}
			],
			"entries": [
				{
					"name": "Naturally Stealthy",
					"entries": [
						"You can attempt to hide even when you are obscured only by a creature that is at least one size larger than you."
					],
					"type": "entries"
				}
			],
			"hasFluff": true,
			"hasFluffImages": true
		},
		{
			"name": "Lotusden",
			"source": "EGW",
			"raceName": "Halfling",
			"raceSource": "PHB",
			"page": 164,
			"ability": [
				{
					"wis": 1
				}
			],
			"additionalSpells": [
				{
					"innate": {
						"3": {
							"daily": {
								"1": [
									"entangle"
								]
							}
						},
						"5": {
							"daily": {
								"1": [
									"spike growth"
								]
							}
						}
					},
					"ability": "wis",
					"known": {
						"1": [
							"druidcraft#c"
						]
					}
				}
			],
			"entries": [
				{
					"type": "entries",
					"name": "Child of the Wood",
					"entries": [
						"You know the {@spell druidcraft} cantrip. When you reach 3rd level, you can cast the {@spell entangle} spell once with this trait and regain the ability to do so when you finish a long rest. When you reach 5th level, you can cast the {@spell spike growth} spell once with this trait and regain the ability to do so when you finish a long rest. Casting these spells with this trait doesn't require material components. Wisdom is your spellcasting ability for these spells."
					]
				},
				{
					"type": "entries",
					"name": "Timberwalk",
					"entries": [
						"Ability checks made to track you have disadvantage, and you can move across {@quickref difficult terrain||3} made of nonmagical plants and undergrowth without expending extra movement."
					]
				}
			],
			"hasFluff": true,
			"hasFluffImages": true
		},
		{
			"name": "Mark of Healing",
			"source": "ERLW",
			"raceName": "Halfling",
			"raceSource": "PHB",
			"page": 43,
			"otherSources": [
				{
					"source": "UAWGE",
					"page": 99
				}
			],
			"ability": [
				{
					"wis": 1
				}
			],
			"traitTags": [
				"Dragonmark",
				"Skill Bonus Dice",
				"Tool Bonus Dice"
			],
			"additionalSpells": [
				{
					"innate": {
						"1": [
							"cure wounds"
						],
						"3": {
							"daily": {
								"1": [
									"lesser restoration"
								]
							}
						}
					},
					"expanded": {
						"s1": [
							"cure wounds",
							"healing word"
						],
						"s2": [
							"lesser restoration",
							"prayer of healing"
						],
						"s3": [
							"aura of vitality",
							"mass healing word"
						],
						"s4": [
							"aura of purity",
							"aura of life"
						],
						"s5": [
							"greater restoration"
						]
					},
					"ability": "wis"
				}
			],
			"entries": [
				{
					"type": "entries",
					"name": "Medical Intuition",
					"entries": [
						"When you make a Wisdom ({@skill Medicine}) check or an ability check using an {@item herbalism kit|phb}, you can roll a {@dice d4} and add the number rolled to the ability check."
					]
				},
				{
					"type": "entries",
					"name": "Healing Touch",
					"entries": [
						"You can cast the {@spell cure wounds} spell with this trait. Starting at 3rd level, you can also cast {@spell lesser restoration} with it. Once you cast either spell with this trait, you can't cast that spell with it again until you finish a long rest. Wisdom is your spellcasting ability for these spells."
					]
				},
				{
					"type": "entries",
					"name": "Spells of the Mark",
					"entries": [
						"If you have the Spellcasting or the Pact Magic class feature, the spells on the Mark of Healing Spells table are added to the spell list of your spellcasting class.",
						{
							"type": "table",
							"caption": "Mark of Healing Spells",
							"colLabels": [
								"Spell Level",
								"Spells"
							],
							"colStyles": [
								"col-2 text-center",
								"col-10"
							],
							"rows": [
								[
									"1st",
									"{@spell cure wounds}, {@spell healing word}"
								],
								[
									"2nd",
									"{@spell lesser restoration}, {@spell prayer of healing}"
								],
								[
									"3rd",
									"{@spell aura of vitality}, {@spell mass healing word}"
								],
								[
									"4th",
									"{@spell aura of purity}, {@spell aura of life}"
								],
								[
									"5th",
									"{@spell greater restoration}"
								]
							]
						}
					]
				}
			]
		},
		{
			"name": "Mark of Hospitality",
			"source": "ERLW",
			"raceName": "Halfling",
			"raceSource": "PHB",
			"page": 44,
			"otherSources": [
				{
					"source": "UAWGE",
					"page": 100
				}
			],
			"ability": [
				{
					"cha": 1
				}
			],
			"traitTags": [
				"Dragonmark",
				"Skill Bonus Dice",
				"Tool Bonus Dice"
			],
			"additionalSpells": [
				{
					"expanded": {
						"s1": [
							"goodberry",
							"sleep"
						],
						"s2": [
							"aid",
							"calm emotions"
						],
						"s3": [
							"create food and water",
							"leomund's tiny hut"
						],
						"s4": [
							"aura of purity",
							"mordenkainen's private sanctum"
						],
						"s5": [
							"hallow"
						]
					},
					"ability": "cha",
					"known": {
						"1": [
							"prestidigitation#c",
							"purify food and drink",
							"unseen servant"
						]
					}
				}
			],
			"entries": [
				{
					"type": "entries",
					"name": "Ever Hospitable",
					"entries": [
						"When you make a Charisma ({@skill Persuasion}) check or an ability check involving {@item brewer's supplies|PHB} or {@item cook's utensils|PHB}, you can roll a {@dice d4} and add the number rolled to the ability check."
					]
				},
				{
					"type": "entries",
					"name": "Innkeeper's Magic",
					"entries": [
						"You know the {@spell prestidigitation} cantrip. You can also cast the {@spell purify food and drink} and {@spell unseen servant} spells with this trait. Once you cast either spell with this trait, you can't cast that spell with it again until you finish long rest. Charisma is your spellcasting ability for these spells."
					]
				},
				{
					"type": "entries",
					"name": "Spells of the Mark",
					"entries": [
						"If you have the Spellcasting or the Pact Magic class feature, the spells on the Mark of Hospitality Spells table are added to the spell list of your spellcasting class.",
						{
							"type": "table",
							"caption": "Mark of Hospitality Spells",
							"colLabels": [
								"Spell Level",
								"Spells"
							],
							"colStyles": [
								"col-2 text-center",
								"col-10"
							],
							"rows": [
								[
									"1st",
									"{@spell goodberry}, {@spell sleep}"
								],
								[
									"2nd",
									"{@spell aid}, {@spell calm emotions}"
								],
								[
									"3rd",
									"{@spell create food and water}, {@spell Leomund's tiny hut}"
								],
								[
									"4th",
									"{@spell aura of purity}, {@spell Mordenkainen's private sanctum}"
								],
								[
									"5th",
									"{@spell hallow}"
								]
							]
						}
					]
				}
			]
		},
		{
			"name": "Stout",
			"source": "PHB",
			"raceName": "Halfling",
			"raceSource": "PHB",
			"page": 28,
			"basicRules": true,
			"ability": [
				{
					"con": 1
				}
			],
			"resist": [
				"poison"
			],
			"entries": [
				{
					"name": "Stout Resilience",
					"entries": [
						"You have advantage on saving throws against poison, and you have resistance against poison damage."
					],
					"type": "entries"
				}
			],
			"hasFluff": true,
			"hasFluffImages": true
		},
		{
			"source": "PHB",
			"raceName": "Human",
			"raceSource": "PHB",
			"page": 29,
			"basicRules": true,
			"ability": [
				{
					"str": 1,
					"dex": 1,
					"con": 1,
					"int": 1,
					"wis": 1,
					"cha": 1
				}
			],
			"hasFluff": true,
			"hasFluffImages": true
		},
		{
			"name": "Keldon",
			"source": "PSD",
			"raceName": "Human",
			"raceSource": "PHB",
			"page": 19,
			"ability": [
				{
					"str": 2,
					"con": 1
				}
			],
			"age": {
				"mature": 20,
				"max": 100
			},
			"skillProficiencies": [
				{
					"athletics": true
				}
			],
			"languageProficiencies": [
				{
					"common": true,
					"other": true
				}
			],
			"entries": [
				{
					"name": "Age",
					"type": "entries",
					"entries": [
						"Keldons reach adulthood in their late teens and live less than a century."
					],
					"data": {
						"overwrite": "Age"
					}
				},
				{
					"name": "Alignment",
					"type": "entries",
					"entries": [
						"Keldons tend toward chaotic alignments, and many walk a fine line between good and evil."
					],
					"data": {
						"overwrite": "Alignment"
					}
				},
				{
					"type": "entries",
					"name": "Size",
					"entries": [
						"Keldons are taller and heavier than the human norms of other cultures, standing almost universally above 6 feet tall and reaching heights above 7 feet. Your size is Medium."
					],
					"data": {
						"overwrite": "Size"
					}
				},
				{
					"name": "Languages",
					"entries": [
						"You can speak, read, and write Common and Keldon."
					],
					"type": "entries",
					"data": {
						"overwrite": "Languages"
					}
				},
				{
					"type": "entries",
					"name": "Natural Athlete",
					"entries": [
						"You have proficiency in the {@skill Athletics} skill."
					]
				},
				{
					"type": "entries",
					"name": "Keldon Resilience",
					"entries": [
						"You have proficiency in Strength saving throws."
					]
				},
				{
					"type": "entries",
					"name": "Icehaven Born",
					"entries": [
						"You are naturally adapted to cold climates, as described in chapter 5 of the {@i Dungeon Master's Guide}."
					]
				}
			],
			"overwrite": {
				"languageProficiencies": true
			},
			"hasFluff": true,
			"hasFluffImages": true
		},
		{
			"name": "Mark of Handling",
			"source": "ERLW",
			"raceName": "Human",
			"raceSource": "PHB",
			"page": 42,
			"otherSources": [
				{
					"source": "UAWGE",
					"page": 98
				}
			],
			"ability": [
				{
					"wis": 2,
					"choose": {
						"from": [
							"str",
							"dex",
							"con",
							"int",
							"cha"
						],
						"count": 1
					}
				}
			],
			"traitTags": [
				"Dragonmark",
				"Skill Bonus Dice"
			],
			"additionalSpells": [
				{
					"expanded": {
						"s1": [
							"animal friendship",
							"speak with animals"
						],
						"s2": [
							"beast sense",
							"calm emotions"
						],
						"s3": [
							"beacon of hope",
							"conjure animals"
						],
						"s4": [
							"aura of life",
							"dominate beast"
						],
						"s5": [
							"awaken"
						]
					},
					"ability": "wis",
					"known": {
						"1": {
							"rest": {
								"1": [
									"animal friendship",
									"speak with animals"
								]
							}
						}
					}
				}
			],
			"entries": [
				{
					"type": "entries",
					"name": "Wild Intuition",
					"entries": [
						"When you make a Wisdom ({@skill Animal Handling}) or Intelligence ({@skill Nature}) check, you can roll a {@dice d4} and add the number rolled to the ability check."
					]
				},
				{
					"type": "entries",
					"name": "Primal Connection",
					"entries": [
						"You can cast the {@spell animal friendship} and {@spell speak with animals} spells with this trait, requiring no material component. Once you cast either spell with this trait, you can't cast that spell with it again until you finish a short or long rest. Wisdom is your spellcasting ability for these spells."
					]
				},
				{
					"type": "entries",
					"name": "The Bigger They Are",
					"entries": [
						"Starting at 3rd level, you can target a beast or monstrosity when you cast {@spell animal friendship} or {@spell speak with animals}, provided the creature's Intelligence score is 3 or lower."
					]
				},
				{
					"type": "entries",
					"name": "Spells of the Mark",
					"entries": [
						"If you have the Spellcasting or the Pact Magic class feature, the spells on the Mark of Handling Spells table are added to the spell list of your spellcasting class.",
						{
							"type": "table",
							"caption": "Mark of Handling Spells",
							"colLabels": [
								"Spell Level",
								"Spells"
							],
							"colStyles": [
								"col-2 text-center",
								"col-10"
							],
							"rows": [
								[
									"1st",
									"{@spell animal friendship}, {@spell speak with animals}"
								],
								[
									"2nd",
									"{@spell beast sense}, {@spell calm emotions}"
								],
								[
									"3rd",
									"{@spell beacon of hope}, {@spell conjure animals}"
								],
								[
									"4th",
									"{@spell aura of life}, {@spell dominate beast}"
								],
								[
									"5th",
									"{@spell awaken}"
								]
							]
						}
					]
				}
			]
		},
		{
			"name": "Mark of Making",
			"source": "ERLW",
			"raceName": "Human",
			"raceSource": "PHB",
			"page": 45,
			"otherSources": [
				{
					"source": "UAWGE",
					"page": 101
				}
			],
			"ability": [
				{
					"int": 2,
					"choose": {
						"from": [
							"str",
							"dex",
							"con",
							"wis",
							"cha"
						],
						"count": 1
					}
				}
			],
			"traitTags": [
				"Dragonmark",
				"Skill Bonus Dice",
				"Tool Bonus Dice"
			],
			"toolProficiencies": [
				{
					"anyArtisans": 1
				}
			],
			"additionalSpells": [
				{
					"expanded": {
						"s1": [
							"identify",
							"tenser's floating disk"
						],
						"s2": [
							"continual flame",
							"magic weapon"
						],
						"s3": [
							"conjure barrage",
							"elemental weapon"
						],
						"s4": [
							"fabricate",
							"stone shape"
						],
						"s5": [
							"creation"
						]
					},
					"ability": "int",
					"known": {
						"1": [
							"mending#c",
							"magic weapon"
						]
					}
				}
			],
			"entries": [
				{
					"type": "entries",
					"name": "Artisan's Intuition",
					"entries": [
						"When you make an {@skill Arcana} check or an ability check involving {@filter artisan's tools|items|source=phb|miscellaneous=mundane|type=artisan's tools}, you can roll a {@dice d4} and add the number rolled to the ability check."
					]
				},
				{
					"type": "entries",
					"name": "Maker's Gift",
					"entries": [
						"You gain proficiency with one type of artisan's tools of your choice."
					]
				},
				{
					"type": "entries",
					"name": "Spellsmith",
					"entries": [
						"You know the {@spell mending} cantrip. You can also cast the {@spell magic weapon} spell with this trait. When you do so, the spell lasts for 1 hour and doesn't require {@status concentration}. Once you cast the spell with this trait, you can't do so again until you finish a long rest. Intelligence is your spellcasting ability for these spells."
					]
				},
				{
					"type": "entries",
					"name": "Spells of the Mark",
					"entries": [
						"If you have the Spellcasting or the Pact Magic class feature, the spells on the Mark of Making Spells table are added to the spell list of your spellcasting class.",
						{
							"type": "table",
							"caption": "Mark of Making Spells",
							"colLabels": [
								"Spell Level",
								"Spells"
							],
							"colStyles": [
								"col-2 text-center",
								"col-10"
							],
							"rows": [
								[
									"1st",
									"{@spell identify}, {@spell Tenser's floating disk}"
								],
								[
									"2nd",
									"{@spell continual flame}, {@spell magic weapon}"
								],
								[
									"3rd",
									"{@spell conjure barrage}, {@spell elemental weapon}"
								],
								[
									"4th",
									"{@spell fabricate}, {@spell stone shape}"
								],
								[
									"5th",
									"{@spell creation}"
								]
							]
						}
					]
				}
			]
		},
		{
			"name": "Mark of Passage",
			"source": "ERLW",
			"raceName": "Human",
			"raceSource": "PHB",
			"page": 46,
			"otherSources": [
				{
					"source": "UAWGE",
					"page": 102
				}
			],
			"speed": 35,
			"ability": [
				{
					"dex": 2,
					"choose": {
						"from": [
							"str",
							"con",
							"int",
							"wis",
							"cha"
						],
						"count": 1
					}
				}
			],
			"traitTags": [
				"Dragonmark"
			],
			"additionalSpells": [
				{
					"expanded": {
						"s1": [
							"expeditious retreat",
							"jump"
						],
						"s2": [
							"misty step",
							"pass without trace"
						],
						"s3": [
							"blink",
							"phantom steed"
						],
						"s4": [
							"dimension door",
							"freedom of movement"
						],
						"s5": [
							"teleportation circle"
						]
					},
					"ability": "dex",
					"known": {
						"1": [
							"misty step"
						]
					}
				}
			],
			"entries": [
				{
					"type": "entries",
					"name": "Courier's Speed",
					"entries": [
						"Your base walking speed increases to 35 feet."
					]
				},
				{
					"type": "entries",
					"name": "Intuitive Motion",
					"entries": [
						"When you make a Dexterity ({@skill Acrobatics}) check or any ability check to operate or maintain a {@filter land vehicle|items|source=phb;dmg|miscellaneous=mundane|type=vehicle (land)}, you can roll a {@dice d4} and add the number rolled to the ability check."
					]
				},
				{
					"type": "entries",
					"name": "Magical Passage",
					"entries": [
						"You can cast the {@spell misty step} spell once with this trait, and you regain the ability to cast it when you finish a long rest. Dexterity is your spellcasting ability for this spell."
					]
				},
				{
					"type": "entries",
					"name": "Spells of the Mark",
					"entries": [
						"If you have the Spellcasting or the Pact Magic class feature, the spells on the Mark of Passage Spells table are added to the spell list of your spellcasting class.",
						{
							"type": "table",
							"caption": "Mark of Passage Spells",
							"colLabels": [
								"Spell Level",
								"Spells"
							],
							"colStyles": [
								"col-2 text-center",
								"col-10"
							],
							"rows": [
								[
									"1st",
									"{@spell expeditious retreat}, {@spell jump}"
								],
								[
									"2nd",
									"{@spell misty step}, {@spell pass without trace}"
								],
								[
									"3rd",
									"{@spell blink}, {@spell phantom steed}"
								],
								[
									"4th",
									"{@spell dimension door}, {@spell freedom of movement}"
								],
								[
									"5th",
									"{@spell teleportation circle}"
								]
							]
						}
					]
				}
			]
		},
		{
			"name": "Mark of Sentinel",
			"source": "ERLW",
			"raceName": "Human",
			"raceSource": "PHB",
			"page": 48,
			"otherSources": [
				{
					"source": "UAWGE",
					"page": 104
				}
			],
			"ability": [
				{
					"con": 2,
					"wis": 1
				}
			],
			"traitTags": [
				"Dragonmark",
				"Skill Bonus Dice"
			],
			"additionalSpells": [
				{
					"expanded": {
						"s1": [
							"compelled duel",
							"shield of faith"
						],
						"s2": [
							"warding bond",
							"zone of truth"
						],
						"s3": [
							"counterspell",
							"protection from energy"
						],
						"s4": [
							"death ward",
							"guardian of faith"
						],
						"s5": [
							"bigby's hand"
						]
					},
					"ability": "wis",
					"known": {
						"1": [
							"shield"
						]
					}
				}
			],
			"entries": [
				{
					"type": "entries",
					"name": "Sentinel's Intuition",
					"entries": [
						"When you make a Wisdom ({@skill Insight}) or Wisdom ({@skill Perception}) check, you can roll a {@dice d4} and add the number rolled to the ability check."
					]
				},
				{
					"type": "entries",
					"name": "Guardian's Shield",
					"entries": [
						"You can cast the {@spell shield} spell once with this trait, and you regain the ability to cast it after you finish a long rest. Wisdom is your spellcasting ability for this spell."
					]
				},
				{
					"type": "entries",
					"name": "Vigilant Guardian",
					"entries": [
						"When a creature you can see within 5 feet of you is hit by an attack roll, you can use your reaction to swap places with that creature, and you are hit by the attack instead. Once you use this trait, you can't do so again until you finish a long rest."
					]
				},
				{
					"type": "entries",
					"name": "Spells of the Mark",
					"entries": [
						"If you have the Spellcasting or the Pact Magic class feature, the spells on the Mark of Sentinel Spells table are added to the spell list of your spellcasting class.",
						{
							"type": "table",
							"caption": "Mark of Sentinel Spells",
							"colLabels": [
								"Spell Level",
								"Spells"
							],
							"colStyles": [
								"col-2 text-center",
								"col-10"
							],
							"rows": [
								[
									"1st",
									"{@spell compelled duel}, {@spell shield of faith}"
								],
								[
									"2nd",
									"{@spell warding bond}, {@spell zone of truth}"
								],
								[
									"3rd",
									"{@spell counterspell}, {@spell protection from energy}"
								],
								[
									"4th",
									"{@spell death ward}, {@spell guardian of faith}"
								],
								[
									"5th",
									"{@spell Bigby's hand}"
								]
							]
						}
					]
				}
			]
		},
		{
			"name": "Variant",
			"source": "PHB",
			"raceName": "Human",
			"raceSource": "PHB",
			"page": 31,
			"basicRules": true,
			"ability": [
				{
					"choose": {
						"from": [
							"str",
							"dex",
							"con",
							"int",
							"wis",
							"cha"
						],
						"count": 2
					}
				}
			],
			"feats": [
				{
					"any": 1
				}
			],
			"skillProficiencies": [
				{
					"any": 1
				}
			],
			"entries": [
				{
					"name": "Skills",
					"entries": [
						"You gain proficiency in one skill of your choice."
					],
					"type": "entries"
				},
				{
					"name": "Feat",
					"entries": [
						"You gain one {@5etools feat|feats.html} of your choice."
					],
					"type": "entries"
				}
			]
		},
		{
			"name": "Variant; Mark of Finding",
			"source": "ERLW",
			"raceName": "Human",
			"raceSource": "PHB",
			"page": 41,
			"ability": [
				{
					"con": 1,
					"wis": 2
				}
			],
			"darkvision": 60,
			"traitTags": [
				"Dragonmark",
				"Skill Bonus Dice"
			],
			"languageProficiencies": [
				{
					"common": true,
					"goblin": true
				}
			],
			"additionalSpells": [
				{
					"innate": {
						"1": [
							"hunter's mark"
						],
						"3": {
							"daily": {
								"1": [
									"locate object"
								]
							}
						}
					},
					"expanded": {
						"s1": [
							"faerie fire",
							"longstrider"
						],
						"s2": [
							"locate animals or plants",
							"locate object"
						],
						"s3": [
							"clairvoyance",
							"speak with plants"
						],
						"s4": [
							"divination",
							"locate creature"
						],
						"s5": [
							"commune with nature"
						]
					},
					"ability": "wis"
				}
			],
			"entries": [
				{
					"type": "entries",
					"name": "Darkvision",
					"entries": [
						"You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. You can't discern color in darkness, only shades of gray."
					]
				},
				{
					"type": "entries",
					"name": "Hunter's Intuition",
					"entries": [
						"When you make a Wisdom ({@skill Perception}) or Wisdom ({@skill Survival}) check, you can roll a {@dice d4} and add the number rolled to the ability check."
					]
				},
				{
					"type": "entries",
					"name": "Finder's Magic",
					"entries": [
						"You can cast the {@spell hunter's mark} spell with this trait. Starting at 3rd level, you can also cast the {@spell locate object} spell with it. Once you cast either spell with this trait, you can't cast that spell with it again until you finish a long rest. Wisdom is your spellcasting ability for these spells."
					]
				},
				{
					"type": "entries",
					"name": "Languages",
					"entries": [
						"You can speak, read, and write Common and Goblin."
					],
					"data": {
						"overwrite": "Languages"
					}
				},
				{
					"type": "entries",
					"name": "Spells of the Mark",
					"entries": [
						"If you have the Spellcasting or the Pact Magic class feature, the spells on the Mark of Finding Spells table are added to the spell list of your spellcasting class.",
						{
							"type": "table",
							"caption": "Mark of Finding Spells",
							"colLabels": [
								"Spell Level",
								"Spells"
							],
							"colStyles": [
								"col-2 text-center",
								"col-10"
							],
							"rows": [
								[
									"1st",
									"{@spell faerie fire}, {@spell longstrider}"
								],
								[
									"2nd",
									"{@spell locate animals or plants}, {@spell locate object}"
								],
								[
									"3rd",
									"{@spell clairvoyance}, {@spell speak with plants}"
								],
								[
									"4th",
									"{@spell divination}, {@spell locate creature}"
								],
								[
									"5th",
									"{@spell commune with nature}"
								]
							]
						}
					]
				}
			],
			"overwrite": {
				"traitTags": true,
				"languageProficiencies": true
			}
		},
		{
			"name": "Gavony",
			"source": "PSI",
			"raceName": "Human (Innistrad)",
			"raceSource": "PSI",
			"page": 8,
			"ability": [
				{
					"str": 1,
					"dex": 1,
					"con": 1,
					"int": 1,
					"wis": 1,
					"cha": 1
				}
			],
			"hasFluff": true,
			"hasFluffImages": true
		},
		{
			"name": "Kessig",
			"source": "PSI",
			"raceName": "Human (Innistrad)",
			"raceSource": "PSI",
			"page": 8,
			"speed": 40,
			"ability": [
				{
					"dex": 1,
					"wis": 1
				}
			],
			"skillProficiencies": [
				{
					"survival": true
				}
			],
			"entries": [
				{
					"name": "Forest Folk",
					"entries": [
						"You have proficiency in the {@skill Survival} skill."
					],
					"type": "entries"
				},
				{
					"name": "Fleet of Foot",
					"entries": [
						"Your base walking speed is 40 feet."
					],
					"type": "entries"
				},
				{
					"name": "Sure-footed",
					"entries": [
						"When you use the {@action Dash} action, {@quickref difficult terrain||3} doesn't cost you extra movement on that turn."
					],
					"type": "entries"
				},
				{
					"name": "Spring Attack",
					"entries": [
						"When you make a melee attack against a creature, you don't provoke opportunity attacks from that creature for the rest of your turn, whether you hit or not."
					],
					"type": "entries"
				}
			],
			"hasFluff": true,
			"hasFluffImages": true
		},
		{
			"name": "Nephalia",
			"source": "PSI",
			"raceName": "Human (Innistrad)",
			"raceSource": "PSI",
			"page": 8,
			"ability": [
				{
					"int": 1,
					"cha": 1
				}
			],
			"traitTags": [
				"Skill Proficiency",
				"Tool Proficiency"
			],
			"skillToolLanguageProficiencies": [
				{
					"choose": [
						{
							"from": [
								"anySkill",
								"anyTool"
							],
							"count": 4
						}
					]
				}
			],
			"entries": [
				{
					"name": "Breadth of Knowledge",
					"entries": [
						"You gain proficiency in any combination of four skills or with four {@book tools|phb|5|tools} of your choice."
					],
					"type": "entries"
				}
			],
			"hasFluff": true,
			"hasFluffImages": true
		},
		{
			"name": "Stensia",
			"source": "PSI",
			"raceName": "Human (Innistrad)",
			"raceSource": "PSI",
			"page": 8,
			"ability": [
				{
					"str": 1,
					"con": 1
				}
			],
			"skillProficiencies": [
				{
					"intimidation": true
				}
			],
			"entries": [
				{
					"name": "Daunting",
					"entries": [
						"You have proficiency in the {@skill Intimidation} skill."
					],
					"type": "entries"
				},
				{
					"name": "Tough",
					"entries": [
						"Your hit point maximum increases by 2, and it increases by 2 every time you gain a level."
					],
					"type": "entries"
				}
			],
			"hasFluff": true,
			"hasFluffImages": true
		},
		{
			"name": "Blue",
			"source": "PSX",
			"raceName": "Merfolk (Ixalan)",
			"raceSource": "PSX",
			"page": 12,
			"ability": [
				{
					"int": 2
				}
			],
			"skillProficiencies": [
				{
					"history": true,
					"nature": true
				}
			],
			"additionalSpells": [
				{
					"ability": "wis",
					"known": {
						"1": {
							"_": [
								{
									"choose": "level=0|class=Wizard"
								}
							]
						}
					}
				}
			],
			"entries": [
				{
					"name": "Cantrip",
					"entries": [
						"You know one cantrip of your choice from the {@filter wizard spell list|spells|class=wizard|level=0}. Intelligence is your spellcasting ability for it."
					],
					"type": "entries"
				},
				{
					"name": "Lore of the Waters",
					"entries": [
						"You gain proficiency in the {@skill History} and {@skill Nature} skills."
					],
					"type": "entries"
				}
			],
			"hasFluff": true,
			"hasFluffImages": true
		},
		{
			"name": "Green",
			"source": "PSX",
			"raceName": "Merfolk (Ixalan)",
			"raceSource": "PSX",
			"page": 12,
			"ability": [
				{
					"wis": 2
				}
			],
			"additionalSpells": [
				{
					"ability": "wis",
					"known": {
						"1": {
							"_": [
								{
									"choose": "level=0|class=Druid"
								}
							]
						}
					}
				}
			],
			"entries": [
				{
					"name": "Cantrip",
					"entries": [
						"You know one cantrip of your choice from the {@filter druid spell list|spells|class=Druid|level=0}. Wisdom is your spellcasting ability for it."
					],
					"type": "entries"
				},
				{
					"name": "Mask of the Wild",
					"entries": [
						"You can attempt to hide even when you are only lightly obscured by foliage, heavy rain, falling snow, mist, and other natural phenomena."
					],
					"type": "entries"
				}
			],
			"hasFluff": true,
			"hasFluffImages": true
		},
		{
			"name": "Cosi Creed",
			"source": "PSZ",
			"raceName": "Merfolk (Zendikar)",
			"raceSource": "PSZ",
			"page": 13,
			"ability": [
				{
					"int": 1,
					"cha": 2
				}
			],
			"skillProficiencies": [
				{
					"sleight of hand": true,
					"stealth": true
				}
			],
			"additionalSpells": [
				{
					"ability": "cha",
					"known": {
						"1": {
							"_": [
								{
									"choose": "level=0|class=Bard"
								}
							]
						}
					}
				}
			],
			"entries": [
				{
					"name": "Cantrip",
					"entries": [
						"You know one cantrip of your choice from the {@filter bard spell list|spells|class=bard|level=0}. Charisma is your spellcasting ability for it."
					],
					"type": "entries"
				},
				{
					"name": "Creed of the Trickster",
					"entries": [
						"You have proficiency in the {@skill Sleight of Hand} and {@skill Stealth} skills."
					],
					"type": "entries"
				}
			],
			"hasFluff": true,
			"hasFluffImages": true
		},
		{
			"name": "Emeria Creed",
			"source": "PSZ",
			"raceName": "Merfolk (Zendikar)",
			"raceSource": "PSZ",
			"page": 13,
			"ability": [
				{
					"wis": 2
				}
			],
			"skillProficiencies": [
				{
					"deception": true,
					"persuasion": true
				}
			],
			"additionalSpells": [
				{
					"ability": "wis",
					"known": {
						"1": {
							"_": [
								{
									"choose": "level=0|class=Druid"
								}
							]
						}
					}
				}
			],
			"entries": [
				{
					"name": "Cantrip",
					"entries": [
						"You know one cantrip of your choice from the {@filter druid spell list|spells|class=druid|level=0}. Wisdom is your spellcasting ability for it."
					],
					"type": "entries"
				},
				{
					"name": "Wind Creed Manipulation",
					"entries": [
						"You have proficiency in the {@skill Deception} and {@skill Persuasion} skills."
					],
					"type": "entries"
				}
			],
			"hasFluff": true,
			"hasFluffImages": true
		},
		{
			"name": "Ula Creed",
			"source": "PSZ",
			"raceName": "Merfolk (Zendikar)",
			"raceSource": "PSZ",
			"page": 13,
			"ability": [
				{
					"int": 2
				}
			],
			"traitTags": [
				"Tool Proficiency"
			],
			"skillProficiencies": [
				{
					"survival": true
				}
			],
			"additionalSpells": [
				{
					"ability": "int",
					"known": {
						"1": {
							"_": [
								{
									"choose": "level=0|class=Wizard"
								}
							]
						}
					}
				}
			],
			"entries": [
				{
					"name": "Cantrip",
					"entries": [
						"You know one cantrip of your choice from the {@filter wizard spell list|spells|class=wizard|level=0}. Intelligence is your spellcasting ability for it."
					],
					"type": "entries"
				},
				{
					"name": "Water Creed Navigation",
					"entries": [
						"You have proficiency with {@item navigator's tools|phb} and in the {@skill Survival} skill."
					],
					"type": "entries"
				}
			],
			"hasFluff": true,
			"hasFluffImages": true
		},
		{
			"name": "Beasthide",
			"source": "ERLW",
			"raceName": "Shifter",
			"raceSource": "ERLW",
			"page": 34,
			"ability": [
				{
					"con": 2,
					"str": 1
				}
			],
			"traitTags": [
				"Natural Armor"
			],
			"skillProficiencies": [
				{
					"athletics": true
				}
			],
			"entries": [
				{
					"type": "entries",
					"name": "Natural Athlete",
					"entries": [
						"You have proficiency in the {@skill Athletics} skill."
					]
				},
				{
					"type": "entries",
					"name": "Shifting Feature",
					"entries": [
						"Whenever you shift, you gain {@dice 1d6} additional temporary hit points. While shifted, you have a +1 bonus to your Armor Class."
					]
				}
			],
			"hasFluff": true,
			"hasFluffImages": true
		},
		{
			"name": "Longtooth",
			"source": "ERLW",
			"raceName": "Shifter",
			"raceSource": "ERLW",
			"page": 34,
			"ability": [
				{
					"str": 2,
					"dex": 1
				}
			],
			"traitTags": [
				"Natural Weapon"
			],
			"skillProficiencies": [
				{
					"intimidation": true
				}
			],
			"entries": [
				{
					"type": "entries",
					"name": "Fierce",
					"entries": [
						"You have proficiency in the {@skill Intimidation} skill."
					]
				},
				{
					"type": "entries",
					"name": "Shifting Feature",
					"entries": [
						"While shifted, you can use your elongated fangs to make an unarmed strike as a bonus action. If you hit with your fangs, you can deal piercing damage equal to {@dice 1d6} + your Strength modifier, instead of the bludgeoning damage normal for an unarmed strike."
					]
				}
			],
			"hasFluff": true,
			"hasFluffImages": true
		},
		{
			"name": "Swiftstride",
			"source": "ERLW",
			"raceName": "Shifter",
			"raceSource": "ERLW",
			"page": 34,
			"ability": [
				{
					"dex": 2,
					"cha": 1
				}
			],
			"skillProficiencies": [
				{
					"acrobatics": true
				}
			],
			"entries": [
				{
					"type": "entries",
					"name": "Graceful",
					"entries": [
						"You have proficiency in the {@skill Acrobatics} skill."
					]
				},
				{
					"type": "entries",
					"name": "Shifting Feature",
					"entries": [
						"While shifted, your walking speed increases by 10 feet. Additionally, you can move up to 10 feet as a reaction when a creature ends its turn within 5 feet of you. This reactive movement doesn't provoke opportunity attacks."
					]
				}
			],
			"hasFluff": true,
			"hasFluffImages": true
		},
		{
			"name": "Wildhunt",
			"source": "ERLW",
			"raceName": "Shifter",
			"raceSource": "ERLW",
			"page": 34,
			"ability": [
				{
					"wis": 2,
					"dex": 1
				}
			],
			"skillProficiencies": [
				{
					"survival": true
				}
			],
			"entries": [
				{
					"type": "entries",
					"name": "Natural Tracker",
					"entries": [
						"You have proficiency in the {@skill Survival} skill."
					]
				},
				{
					"type": "entries",
					"name": "Shifting Feature",
					"entries": [
						"While shifted, you have advantage on Wisdom checks, and no creature within 30 feet of you can make an attack roll with advantage against you, unless you're {@condition incapacitated}."
					]
				}
			],
			"hasFluff": true,
			"hasFluffImages": true
		},
		{
			"name": "Beasthide",
			"source": "UAEberron",
			"raceName": "Shifter",
			"raceSource": "UAEberron",
			"page": 2,
			"reprintedAs": [
				"Shifter (Beasthide)|UARacesOfEberron"
			],
			"ability": [
				{
					"con": 1
				}
			],
			"traitTags": [
				"Natural Armor"
			],
			"entries": [
				{
					"name": "Shifting Feature",
					"entries": [
						"While shifting, you gain a +1 bonus to AC."
					],
					"type": "entries"
				}
			]
		},
		{
			"name": "Cliffwalk",
			"source": "UAEberron",
			"raceName": "Shifter",
			"raceSource": "UAEberron",
			"page": 2,
			"ability": [
				{
					"dex": 2
				}
			],
			"entries": [
				{
					"name": "Shifting Feature",
					"entries": [
						"While shifting, you gain a climb speed of 30 feet."
					],
					"type": "entries"
				}
			]
		},
		{
			"name": "Longstride",
			"source": "UAEberron",
			"raceName": "Shifter",
			"raceSource": "UAEberron",
			"page": 2,
			"ability": [
				{
					"dex": 2
				}
			],
			"entries": [
				{
					"name": "Shifting Feature",
					"entries": [
						"While shifting, you can use the {@action Dash} action as a bonus action."
					],
					"type": "entries"
				}
			]
		},
		{
			"name": "Longtooth",
			"source": "UAEberron",
			"raceName": "Shifter",
			"raceSource": "UAEberron",
			"page": 2,
			"reprintedAs": [
				"Shifter (Longtooth)|UARacesOfEberron"
			],
			"ability": [
				{
					"str": 1
				}
			],
			"entries": [
				{
					"name": "Shifting Feature",
					"entries": [
						"While shifting, you can make a bite attack as an action. This is a melee weapon attack that uses Strength for its attack roll and damage bonus and deals {@dice 1d6} piercing damage. If this attack hits a target that is your size or smaller, the target is also {@condition grappled}."
					],
					"type": "entries"
				}
			]
		},
		{
			"name": "Razorclaw",
			"source": "UAEberron",
			"raceName": "Shifter",
			"raceSource": "UAEberron",
			"page": 2,
			"ability": [
				{
					"dex": 2
				}
			],
			"traitTags": [
				"Natural Weapon"
			],
			"entries": [
				{
					"name": "Shifting Feature",
					"entries": [
						"While shifting, you can make an unarmed strike as a bonus action. You can use your Dexterity for its attack roll and damage bonus, and this attack deals slashing damage."
					],
					"type": "entries"
				}
			]
		},
		{
			"name": "Wildhunt",
			"source": "UAEberron",
			"raceName": "Shifter",
			"raceSource": "UAEberron",
			"page": 3,
			"reprintedAs": [
				"Shifter (Wildhunt)|UARacesOfEberron"
			],
			"ability": [
				{
					"wis": 1
				}
			],
			"entries": [
				{
					"name": "Shifting Feature",
					"entries": [
						"While shifting, you gain advantage on all Wisdom-based checks and saving throws."
					],
					"type": "entries"
				}
			]
		},
		{
			"name": "Beasthide",
			"source": "UARacesOfEberron",
			"raceName": "Shifter",
			"raceSource": "UARacesOfEberron",
			"page": 6,
			"reprintedAs": [
				"Shifter (Beasthide)|ERLW"
			],
			"ability": [
				{
					"con": 2
				}
			],
			"traitTags": [
				"Natural Armor"
			],
			"skillProficiencies": [
				{
					"athletics": true
				}
			],
			"entries": [
				{
					"type": "entries",
					"name": "Tough",
					"entries": [
						"You have proficiency with the {@skill Athletics} skill."
					]
				},
				{
					"type": "entries",
					"name": "Shifting Feature",
					"entries": [
						"Whenever you shift, you gain {@dice 1d6} additional temporary hit points, and while shifted, you have a +1 bonus to your AC."
					]
				}
			]
		},
		{
			"name": "Longtooth",
			"source": "UARacesOfEberron",
			"raceName": "Shifter",
			"raceSource": "UARacesOfEberron",
			"page": 6,
			"reprintedAs": [
				"Shifter (Longtooth)|ERLW"
			],
			"ability": [
				{
					"str": 2
				}
			],
			"traitTags": [
				"Natural Weapon"
			],
			"skillProficiencies": [
				{
					"intimidation": true
				}
			],
			"entries": [
				{
					"type": "entries",
					"name": "Fierce",
					"entries": [
						"You have proficiency with the {@skill Intimidation} skill."
					]
				},
				{
					"type": "entries",
					"name": "Shifting Feature",
					"entries": [
						"While shifted, you can use your elongated fangs to make an unarmed strike as a bonus action. If you hit with your fangs, you can deal piercing damage equal to {@dice 1d6} + your Strength modifier, instead of the bludgeoning damage normal for an unarmed strike."
					]
				}
			]
		},
		{
			"name": "Swiftstride",
			"source": "UARacesOfEberron",
			"raceName": "Shifter",
			"raceSource": "UARacesOfEberron",
			"page": 6,
			"reprintedAs": [
				"Shifter (Swiftstride)|ERLW"
			],
			"speed": 35,
			"ability": [
				{
					"dex": 2,
					"cha": 1
				}
			],
			"skillProficiencies": [
				{
					"acrobatics": true
				}
			],
			"entries": [
				{
					"type": "entries",
					"name": "Graceful",
					"entries": [
						"You have proficiency with the {@skill Acrobatics} skill."
					]
				},
				{
					"type": "entries",
					"name": "Swift Stride",
					"entries": [
						"Your walking speed increases by 5 feet."
					]
				},
				{
					"type": "entries",
					"name": "Shifting Feature",
					"entries": [
						"While shifted, your walking speed increases by 5 feet. Additionally, you can move up to 10 feet as a reaction when an enemy ends its turn within 5 feet of you. This movement doesn't provoke opportunity attacks."
					]
				}
			]
		},
		{
			"name": "Wildhunt",
			"source": "UARacesOfEberron",
			"raceName": "Shifter",
			"raceSource": "UARacesOfEberron",
			"page": 6,
			"reprintedAs": [
				"Shifter (Wildhunt)|ERLW"
			],
			"ability": [
				{
					"wis": 2
				}
			],
			"skillProficiencies": [
				{
					"survival": true
				}
			],
			"entries": [
				{
					"type": "entries",
					"name": "Natural Tracker",
					"entries": [
						"You have proficiency with the {@skill Survival} skill."
					]
				},
				{
					"type": "entries",
					"name": "Mark the Scent",
					"entries": [
						"As a bonus action, you can mark one creature you can see within 10 feet of you. Until the end of your next long rest, your proficiency bonus is doubled for any ability check you make to find the marked creature, and you always know the location of that creature if it is within 60 feet of you. You can't use this trait again until you finish a short or long rest."
					]
				},
				{
					"type": "entries",
					"name": "Shifting Feature",
					"entries": [
						"While shifted, you have advantage on Wisdom checks."
					]
				}
			]
		},
		{
			"source": "PHB",
			"raceName": "Tiefling",
			"raceSource": "PHB",
			"page": 42,
			"srd": true,
			"hasFluff": true,
			"hasFluffImages": true
		},
		{
			"name": "Abyssal",
			"source": "UAThatOldBlackMagic",
			"raceName": "Tiefling",
			"raceSource": "PHB",
			"page": 1,
			"ability": [
				{
					"cha": 2,
					"con": 1
				}
			],
			"traitTags": [
				"Uncommon Race"
			],
			"languageProficiencies": [
				{
					"common": true,
					"abyssal": true
				}
			],
			"resist": null,
			"additionalSpells": [
				{
					"innate": {
						"3": {
							"daily": {
								"1": [
									"burning hands",
									"charm person",
									"magic missile",
									"cure wounds",
									"tasha's hideous laughter",
									"thunderwave"
								]
							}
						},
						"5": {
							"daily": {
								"1": [
									"alter self",
									"darkness",
									"invisibility",
									"levitate",
									"mirror image",
									"spider climb"
								]
							}
						}
					},
					"known": {
						"1": [
							"dancing lights#c",
							"true strike#c",
							"light#c",
							"message#c",
							"spare the dying#c",
							"prestidigitation#c"
						]
					}
				}
			],
			"entries": [
				{
					"name": "Abyssal Arcana",
					"entries": [
						"Each time you finish a long rest, you gain the ability to cast cantrips and spells randomly determined from a short list. At 1st level, you can cast a cantrip. When you reach 3rd level, you can also cast a 1st-level spell. At 5th level, you can cast a 2nd-level spell.",
						"You can cast a spell gained from this trait only once until you complete your next long rest. You can cast a cantrip gained from this trait at will, as normal. For 1st-level spells whose effect changes if cast using a spell slot of 2nd level or higher, you cast the spell as if using a 2nd-level slot. Spells of 2nd level are cast as if using a 2nd-level slot",
						"At the end of each long rest, you lose the cantrips and spells previously granted by this feature, even if you did not cast them. You replace those cantrips and spells by rolling for new ones on the Abyssal Arcana Spells table. Roll separately for each cantrip and spell. If you roll the same spell or cantrip you gained at the end of your previous long rest, roll again until you get a different result.",
						{
							"type": "table",
							"caption": "Abyssal Arcana Spells",
							"colLabels": [
								"d6",
								"1st Level",
								"3rd Level",
								"5th Level"
							],
							"colStyles": [
								"col-1 text-center",
								"col-3-67",
								"col-3-67",
								"col-3-67"
							],
							"rows": [
								[
									"1",
									"{@spell Dancing lights}",
									"{@spell Burning hands}",
									"{@spell Alter self}"
								],
								[
									"2",
									"{@spell True strike}",
									"{@spell Charm person}",
									"{@spell Darkness}"
								],
								[
									"3",
									"{@spell Light}",
									"{@spell Magic missile}",
									"{@spell Invisibility}"
								],
								[
									"4",
									"{@spell Message}",
									"{@spell Cure wounds}",
									"{@spell Levitate}"
								],
								[
									"5",
									"{@spell Spare the dying}",
									"{@spell Tasha's hideous laughter}",
									"{@spell Mirror Image}"
								],
								[
									"6",
									"{@spell Prestidigitation}",
									"{@spell Thunderwave}",
									"{@spell Spider climb}"
								]
							]
						}
					],
					"type": "entries",
					"data": {
						"overwrite": "Infernal Legacy"
					}
				},
				{
					"name": "Abyssal Fortitude",
					"entries": [
						"Your hit point maximum increases by half your level (minimum 1)."
					],
					"data": {
						"overwrite": "Hellish Resistance"
					},
					"type": "entries"
				},
				{
					"name": "Languages",
					"entries": [
						"You can speak, read, and write Common and Abyssal."
					],
					"data": {
						"overwrite": "Languages"
					},
					"type": "entries"
				}
			],
			"overwrite": {
				"languageProficiencies": true,
				"ability": true,
				"traitTags": true
			}
		},
		{
			"name": "Asmodeus",
			"source": "MTF",
			"raceName": "Tiefling",
			"raceSource": "PHB",
			"page": 21,
			"hasFluff": true,
			"hasFluffImages": true
		},
		{
			"name": "Asmodeus",
			"source": "UAFiendishOptions",
			"raceName": "Tiefling",
			"raceSource": "PHB",
			"page": 1,
			"srd": true,
			"reprintedAs": [
				"Tiefling (Asmodeus)|MTF"
			]
		},
		{
			"name": "Baalzebul",
			"source": "MTF",
			"raceName": "Tiefling",
			"raceSource": "PHB",
			"page": 21,
			"additionalSpells": [
				{
					"innate": {
						"3": {
							"daily": {
								"1": [
									"ray of sickness#2"
								]
							}
						},
						"5": {
							"daily": {
								"1": [
									"crown of madness"
								]
							}
						}
					},
					"ability": "cha",
					"known": {
						"1": [
							"thaumaturgy#c"
						]
					}
				}
			],
			"entries": [
				{
					"name": "Legacy of Maladomini",
					"entries": [
						"You know the {@spell thaumaturgy} cantrip. When you reach 3rd level, you can cast the {@spell ray of sickness} spell as a 2nd-level spell once with this trait and regain the ability to do so when you finish a long rest. When you reach 5th level, you can cast the {@spell crown of madness} spell once with this trait and regain the ability to do so when you finish a long rest. Charisma is your spellcasting ability for these spells."
					],
					"type": "entries",
					"data": {
						"overwrite": "Infernal Legacy"
					}
				}
			],
			"hasFluff": true,
			"hasFluffImages": true
		},
		{
			"name": "Baalzebul",
			"source": "UAFiendishOptions",
			"raceName": "Tiefling",
			"raceSource": "PHB",
			"page": 1,
			"reprintedAs": [
				"Tiefling (Baalzebul)|MTF"
			],
			"additionalSpells": [
				{
					"innate": {
						"3": {
							"daily": {
								"1": [
									"ray of sickness#2"
								]
							}
						},
						"5": {
							"daily": {
								"1": [
									"crown of madness"
								]
							}
						}
					},
					"ability": "cha",
					"known": {
						"1": [
							"thaumaturgy#c"
						]
					}
				}
			],
			"entries": [
				{
					"name": "Legacy of Maladomini",
					"entries": [
						"You know the {@spell thaumaturgy} cantrip. When you reach 3rd level, you can cast the {@spell ray of sickness} spell as a 2nd-level spell once with this trait and regain the ability to do so when you finish a long rest. When you reach 5th level, you can cast the {@spell crown of madness} spell once with this trait and regain the ability to do so when you finish a long rest. Charisma is your spellcasting ability for these spells."
					],
					"type": "entries",
					"data": {
						"overwrite": "Infernal Legacy"
					}
				}
			]
		},
		{
			"name": "Dispater",
			"source": "MTF",
			"raceName": "Tiefling",
			"raceSource": "PHB",
			"page": 21,
			"ability": [
				{
					"cha": 2,
					"dex": 1
				}
			],
			"additionalSpells": [
				{
					"innate": {
						"3": {
							"daily": {
								"1": [
									"disguise self"
								]
							}
						},
						"5": {
							"daily": {
								"1": [
									"detect thoughts"
								]
							}
						}
					},
					"ability": "cha",
					"known": {
						"1": [
							"thaumaturgy#c"
						]
					}
				}
			],
			"entries": [
				{
					"name": "Legacy of Dis",
					"entries": [
						"You know the {@spell thaumaturgy} cantrip. When you reach 3rd level, you can cast the {@spell disguise self} spell once with this trait and regain the ability to do so when you finish a long rest. When you reach 5th level, you can cast the {@spell detect thoughts} spell once with this trait and regain the ability to do so when you finish a long rest. Charisma is your spellcasting ability for these spells."
					],
					"type": "entries",
					"data": {
						"overwrite": "Infernal Legacy"
					}
				}
			],
			"overwrite": {
				"ability": true
			},
			"hasFluff": true,
			"hasFluffImages": true
		},
		{
			"name": "Dispater",
			"source": "UAFiendishOptions",
			"raceName": "Tiefling",
			"raceSource": "PHB",
			"page": 1,
			"reprintedAs": [
				"Tiefling (Dispater)|MTF"
			],
			"ability": [
				{
					"cha": 2,
					"dex": 1
				}
			],
			"additionalSpells": [
				{
					"innate": {
						"3": {
							"daily": {
								"1": [
									"disguise self"
								]
							}
						},
						"5": {
							"daily": {
								"1": [
									"invisibility"
								]
							}
						}
					},
					"ability": "cha",
					"known": {
						"1": [
							"thaumaturgy#c"
						]
					}
				}
			],
			"entries": [
				{
					"name": "Legacy of Dis",
					"entries": [
						"You know the {@spell thaumaturgy} cantrip. When you reach 3rd level, you can cast the {@spell disguise self} spell once with this trait and regain the ability to do so when you finish a long rest. When you reach 5th level, you can cast the {@spell invisibility} spell once with this trait and regain the ability to do so when you finish a long rest. Charisma is your spellcasting ability for these spells."
					],
					"type": "entries",
					"data": {
						"overwrite": "Infernal Legacy"
					}
				}
			],
			"overwrite": {
				"ability": true
			}
		},
		{
			"name": "Fierna",
			"source": "MTF",
			"raceName": "Tiefling",
			"raceSource": "PHB",
			"page": 21,
			"ability": [
				{
					"cha": 2,
					"wis": 1
				}
			],
			"additionalSpells": [
				{
					"innate": {
						"3": {
							"daily": {
								"1": [
									"charm person#2"
								]
							}
						},
						"5": {
							"daily": {
								"1": [
									"suggestion"
								]
							}
						}
					},
					"ability": "cha",
					"known": {
						"1": [
							"friends#c"
						]
					}
				}
			],
			"entries": [
				{
					"name": "Legacy of Phlegethos",
					"entries": [
						"You know the {@spell friends} cantrip. When you reach 3rd level, you can cast the {@spell charm person} spell as a 2nd-level spell once with this trait and regain the ability to do so when you finish a long rest. When you reach 5th level, you can cast the {@spell suggestion} spell once with this trait and regain the ability to do so when you finish a long rest. Charisma is your spellcasting ability for these spells."
					],
					"type": "entries",
					"data": {
						"overwrite": "Infernal Legacy"
					}
				}
			],
			"overwrite": {
				"ability": true
			},
			"hasFluff": true,
			"hasFluffImages": true
		},
		{
			"name": "Fierna",
			"source": "UAFiendishOptions",
			"raceName": "Tiefling",
			"raceSource": "PHB",
			"page": 1,
			"reprintedAs": [
				"Tiefling (Fierna)|MTF"
			],
			"ability": [
				{
					"cha": 2,
					"wis": 1
				}
			],
			"additionalSpells": [
				{
					"innate": {
						"3": {
							"daily": {
								"1": [
									"charm person#2"
								]
							}
						},
						"5": {
							"daily": {
								"1": [
									"suggestion"
								]
							}
						}
					},
					"ability": "cha",
					"known": {
						"1": [
							"friends#c"
						]
					}
				}
			],
			"entries": [
				{
					"name": "Legacy of Phlegethos",
					"entries": [
						"You know the {@spell friends} cantrip. When you reach 3rd level, you can cast the {@spell charm person} spell as a 2nd-level spell once with this trait and regain the ability to do so when you finish a long rest. When you reach 5th level, you can cast the {@spell suggestion} spell once with this trait and regain the ability to do so when you finish a long rest. Charisma is your spellcasting ability for these spells."
					],
					"type": "entries",
					"data": {
						"overwrite": "Infernal Legacy"
					}
				}
			],
			"overwrite": {
				"ability": true
			}
		},
		{
			"name": "Glasya",
			"source": "MTF",
			"raceName": "Tiefling",
			"raceSource": "PHB",
			"page": 22,
			"ability": [
				{
					"cha": 2,
					"dex": 1
				}
			],
			"additionalSpells": [
				{
					"innate": {
						"3": {
							"daily": {
								"1": [
									"disguise self"
								]
							}
						},
						"5": {
							"daily": {
								"1": [
									"invisibility"
								]
							}
						}
					},
					"ability": "cha",
					"known": {
						"1": [
							"minor illusion#c"
						]
					}
				}
			],
			"entries": [
				{
					"name": "Legacy of Malbolge",
					"entries": [
						"You know the {@spell minor illusion} cantrip. When you reach 3rd level, you can cast the {@spell disguise self} spell once with this trait and regain the ability to do so when you finish a long rest. When you reach 5th level, you can cast the {@spell invisibility} spell once with this trait and regain the ability to do so when you finish a long rest. Charisma is your spellcasting ability for these spells."
					],
					"type": "entries",
					"data": {
						"overwrite": "Infernal Legacy"
					}
				}
			],
			"overwrite": {
				"ability": true
			},
			"hasFluff": true,
			"hasFluffImages": true
		},
		{
			"name": "Glasya",
			"source": "UAFiendishOptions",
			"raceName": "Tiefling",
			"raceSource": "PHB",
			"page": 2,
			"reprintedAs": [
				"Tiefling (Glasya)|MTF"
			],
			"ability": [
				{
					"cha": 2,
					"dex": 1
				}
			],
			"additionalSpells": [
				{
					"innate": {
						"3": {
							"daily": {
								"1": [
									"disguise self"
								]
							}
						},
						"5": {
							"daily": {
								"1": [
									"invisibility"
								]
							}
						}
					},
					"ability": "cha",
					"known": {
						"1": [
							"minor illusion#c"
						]
					}
				}
			],
			"entries": [
				{
					"name": "Legacy of Malbolge",
					"entries": [
						"You know the {@spell minor illusion} cantrip. When you reach 3rd level, you can cast the {@spell disguise self} spell once with this trait and regain the ability to do so when you finish a long rest. When you reach 5th level, you can cast the {@spell invisibility} spell once with this trait and regain the ability to do so when you finish a long rest. Charisma is your spellcasting ability for these spells."
					],
					"type": "entries",
					"data": {
						"overwrite": "Infernal Legacy"
					}
				}
			],
			"overwrite": {
				"ability": true
			}
		},
		{
			"name": "Levistus",
			"source": "MTF",
			"raceName": "Tiefling",
			"raceSource": "PHB",
			"page": 22,
			"ability": [
				{
					"cha": 2,
					"con": 1
				}
			],
			"additionalSpells": [
				{
					"innate": {
						"3": {
							"daily": {
								"1": [
									"armor of agathys#2"
								]
							}
						},
						"5": {
							"daily": {
								"1": [
									"darkness"
								]
							}
						}
					},
					"ability": "cha",
					"known": {
						"1": [
							"ray of frost#c"
						]
					}
				}
			],
			"entries": [
				{
					"name": "Legacy of Stygia",
					"entries": [
						"You know the {@spell ray of frost} cantrip. When you reach 3rd level, you can cast the {@spell armor of Agathys} spell as a 2nd-level spell once with this trait and regain the ability to do so when you finish a long rest. When you reach 5th level, you can cast the {@spell darkness} spell once with this trait and regain the ability to do so when you finish a long rest. Charisma is your spellcasting ability for these spells."
					],
					"type": "entries",
					"data": {
						"overwrite": "Infernal Legacy"
					}
				}
			],
			"overwrite": {
				"ability": true
			},
			"hasFluff": true,
			"hasFluffImages": true
		},
		{
			"name": "Levistus",
			"source": "UAFiendishOptions",
			"raceName": "Tiefling",
			"raceSource": "PHB",
			"page": 2,
			"reprintedAs": [
				"Tiefling (Levistus)|MTF"
			],
			"ability": [
				{
					"cha": 2,
					"con": 1
				}
			],
			"additionalSpells": [
				{
					"innate": {
						"3": {
							"daily": {
								"1": [
									"armor of agathys#2"
								]
							}
						},
						"5": {
							"daily": {
								"1": [
									"darkness"
								]
							}
						}
					},
					"ability": "cha",
					"known": {
						"1": [
							"ray of frost#c"
						]
					}
				}
			],
			"entries": [
				{
					"name": "Legacy of Stygia",
					"entries": [
						"You know the {@spell ray of frost} cantrip. When you reach 3rd level, you can cast the {@spell armor of Agathys} spell as a 2nd-level spell once with this trait and regain the ability to do so when you finish a long rest. When you reach 5th level, you can cast the {@spell darkness} spell once with this trait and regain the ability to do so when you finish a long rest. Charisma is your spellcasting ability for these spells."
					],
					"type": "entries",
					"data": {
						"overwrite": "Infernal Legacy"
					}
				}
			],
			"overwrite": {
				"ability": true
			}
		},
		{
			"name": "Mammon",
			"source": "MTF",
			"raceName": "Tiefling",
			"raceSource": "PHB",
			"page": 22,
			"additionalSpells": [
				{
					"innate": {
						"3": {
							"daily": {
								"1": [
									"tenser's floating disk"
								]
							}
						},
						"5": {
							"daily": {
								"1": [
									"arcane lock"
								]
							}
						}
					},
					"ability": "cha",
					"known": {
						"1": [
							"mage hand#c"
						]
					}
				}
			],
			"entries": [
				{
					"name": "Legacy of Minauros",
					"entries": [
						"You know the {@spell mage hand} cantrip. When you reach 3rd level, you can cast the {@spell Tenser's floating disk} spell once with this trait and regain the ability to do so when you finish a short or long rest. When you reach 5th level, you can cast the {@spell arcane lock} spell once with this trait, requiring no material component, and regain the ability to do so when you finish a long rest. Charisma is your spellcasting ability for these spells."
					],
					"type": "entries",
					"data": {
						"overwrite": "Infernal Legacy"
					}
				}
			],
			"hasFluff": true,
			"hasFluffImages": true
		},
		{
			"name": "Mammon",
			"source": "UAFiendishOptions",
			"raceName": "Tiefling",
			"raceSource": "PHB",
			"page": 2,
			"reprintedAs": [
				"Tiefling (Mammon)|MTF"
			],
			"additionalSpells": [
				{
					"innate": {
						"3": {
							"daily": {
								"1": [
									"tenser's floating disk"
								]
							}
						},
						"5": {
							"daily": {
								"1": [
									"arcane lock"
								]
							}
						}
					},
					"ability": "cha",
					"known": {
						"1": [
							"mage hand#c"
						]
					}
				}
			],
			"entries": [
				{
					"name": "Legacy of Minauros",
					"entries": [
						"You know the {@spell mage hand} cantrip. When you reach 3rd level, you can cast the {@spell Tenser's floating disk} spell once with this trait and regain the ability to do so when you finish a short or long rest. When you reach 5th level, you can cast the {@spell arcane lock} spell once with this trait, requiring no material component, and regain the ability to do so when you finish a long rest. Charisma is your spellcasting ability for these spells."
					],
					"type": "entries",
					"data": {
						"overwrite": "Infernal Legacy"
					}
				}
			]
		},
		{
			"name": "Mephistopheles",
			"source": "MTF",
			"raceName": "Tiefling",
			"raceSource": "PHB",
			"page": 23,
			"additionalSpells": [
				{
					"innate": {
						"3": {
							"daily": {
								"1": [
									"burning hands#2"
								]
							}
						},
						"5": {
							"daily": {
								"1": [
									"flame blade"
								]
							}
						}
					},
					"ability": "cha",
					"known": {
						"1": [
							"mage hand#c"
						]
					}
				}
			],
			"entries": [
				{
					"name": "Legacy of Cania",
					"entries": [
						"You know the {@spell mage hand} cantrip. When you reach 3rd level, you can cast the {@spell burning hands} spell as a 2nd-level spell once with this trait and regain the ability to do so when you finish a long rest. When you reach 5th level, you can cast the {@spell flame blade} spell once with this trait and regain the ability to do so when you finish a long rest. Charisma is your spellcasting ability for these spells."
					],
					"type": "entries",
					"data": {
						"overwrite": "Infernal Legacy"
					}
				}
			],
			"hasFluff": true,
			"hasFluffImages": true
		},
		{
			"name": "Mephistopheles",
			"source": "UAFiendishOptions",
			"raceName": "Tiefling",
			"raceSource": "PHB",
			"page": 2,
			"reprintedAs": [
				"Tiefling (Mephistopheles)|MTF"
			],
			"additionalSpells": [
				{
					"innate": {
						"3": {
							"daily": {
								"1": [
									"magic missile#2"
								]
							}
						},
						"5": {
							"daily": {
								"1": [
									"web"
								]
							}
						}
					},
					"ability": "cha",
					"known": {
						"1": [
							"mage hand#c"
						]
					}
				}
			],
			"entries": [
				{
					"name": "Legacy of Cania",
					"entries": [
						"You know the {@spell mage hand} cantrip. When you reach 3rd level, you can cast the {@spell magic missile} spell as a 2nd-level spell once with this trait and regain the ability to do so when you finish a long rest. When you reach 5th level, you can cast the {@spell web} spell once with this trait and regain the ability to do so when you finish a long rest. Charisma is your spellcasting ability for these spells."
					],
					"type": "entries",
					"data": {
						"overwrite": "Infernal Legacy"
					}
				}
			]
		},
		{
			"name": "Variant; Devil's Tongue",
			"source": "SCAG",
			"raceName": "Tiefling",
			"raceSource": "PHB",
			"page": 118,
			"ability": [
				{
					"int": 1,
					"choose": {
						"from": [
							"dex",
							"cha"
						],
						"count": 1,
						"amount": 2
					}
				}
			],
			"additionalSpells": [
				{
					"innate": {
						"3": {
							"daily": {
								"1": [
									"charm person#2"
								]
							}
						},
						"5": {
							"daily": {
								"1": [
									"enthrall"
								]
							}
						}
					},
					"ability": "cha",
					"known": {
						"1": [
							"vicious mockery#c"
						]
					}
				}
			],
			"entries": [
				{
					"name": "Appearance",
					"entries": [
						"Your tiefling might not look like other tieflings. Rather than having the physical characteristics described in the Player's Handbook, choose {@dice 1d4+1} of the following features: small horns; fangs or sharp teeth; a forked tongue; catlike eyes; six fingers on each hand; goatlike legs; cloven hoofs; a forked tail; leathery or scaly skin; red or dark blue skin; cast no shadow or reflection; exude a smell of brimstone."
					],
					"type": "entries"
				},
				{
					"type": "entries",
					"name": "Devil's Tongue",
					"entries": [
						"You know the {@spell vicious mockery} cantrip. When you reach 3rd level, you can cast the {@spell charm person} spell as a 2nd-level spell once with this trait. When you reach 5th level, you can cast the {@spell enthrall} spell once with this trait. You must finish a long rest to cast these spells once again with this trait. Charisma is your spellcasting ability for them. This trait replaces the Infernal Legacy trait."
					],
					"data": {
						"overwrite": "Infernal Legacy"
					}
				}
			],
			"overwrite": {
				"ability": true
			},
			"hasFluff": true,
			"hasFluffImages": true
		},
		{
			"name": "Variant; Hellfire",
			"source": "SCAG",
			"raceName": "Tiefling",
			"raceSource": "PHB",
			"page": 118,
			"ability": [
				{
					"int": 1,
					"choose": {
						"from": [
							"dex",
							"cha"
						],
						"count": 1,
						"amount": 2
					}
				}
			],
			"additionalSpells": [
				{
					"innate": {
						"3": {
							"daily": {
								"1": [
									"burning hands#2"
								]
							}
						},
						"5": {
							"daily": {
								"1": [
									"darkness"
								]
							}
						}
					},
					"ability": "cha",
					"known": {
						"1": [
							"thaumaturgy#c"
						]
					}
				}
			],
			"entries": [
				{
					"name": "Appearance",
					"entries": [
						"Your tiefling might not look like other tieflings. Rather than having the physical characteristics described in the Player's Handbook, choose {@dice 1d4+1} of the following features: small horns; fangs or sharp teeth; a forked tongue; catlike eyes; six fingers on each hand; goatlike legs; cloven hoofs; a forked tail; leathery or scaly skin; red or dark blue skin; cast no shadow or reflection; exude a smell of brimstone."
					],
					"type": "entries"
				},
				{
					"type": "entries",
					"name": "Hellfire",
					"entries": [
						"You know the {@spell thaumaturgy} cantrip. Once you reach 3rd level, you can cast the {@spell burning hands} spell once per day as a 2nd-level spell; you must finish a long rest in order to cast the spell again using this trait. Once you reach 5th level, you can also cast the {@spell darkness} spell; you must finish a long rest in order to cast the spell again using this trait. Charisma is your spellcasting ability for these spells."
					],
					"data": {
						"overwrite": "Infernal Legacy"
					}
				}
			],
			"overwrite": {
				"ability": true
			},
			"hasFluff": true,
			"hasFluffImages": true
		},
		{
			"name": "Variant; Infernal Legacy",
			"source": "SCAG",
			"raceName": "Tiefling",
			"raceSource": "PHB",
			"page": 118,
			"ability": [
				{
					"int": 1,
					"choose": {
						"from": [
							"dex",
							"cha"
						],
						"count": 1,
						"amount": 2
					}
				}
			],
			"additionalSpells": [
				{
					"innate": {
						"3": {
							"daily": {
								"1": [
									"hellish rebuke"
								]
							}
						},
						"5": {
							"daily": {
								"1": [
									"darkness"
								]
							}
						}
					},
					"ability": "cha",
					"known": {
						"1": [
							"thaumaturgy#c"
						]
					}
				}
			],
			"entries": [
				{
					"name": "Appearance",
					"entries": [
						"Your tiefling might not look like other tieflings. Rather than having the physical characteristics described in the Player's Handbook, choose {@dice 1d4+1} of the following features: small horns; fangs or sharp teeth; a forked tongue; catlike eyes; six fingers on each hand; goatlike legs; cloven hoofs; a forked tail; leathery or scaly skin; red or dark blue skin; cast no shadow or reflection; exude a smell of brimstone."
					],
					"type": "entries"
				}
			],
			"overwrite": {
				"ability": true
			},
			"hasFluff": true,
			"hasFluffImages": true
		},
		{
			"name": "Variant; Winged",
			"source": "SCAG",
			"raceName": "Tiefling",
			"raceSource": "PHB",
			"page": 118,
			"speed": {
				"walk": 30,
				"fly": 30
			},
			"ability": [
				{
					"int": 1,
					"choose": {
						"from": [
							"dex",
							"cha"
						],
						"count": 1,
						"amount": 2
					}
				}
			],
			"traitTags": [
				"Uncommon Race"
			],
			"additionalSpells": null,
			"entries": [
				{
					"name": "Appearance",
					"entries": [
						"Your tiefling might not look like other tieflings. Rather than having the physical characteristics described in the Player's Handbook, choose {@dice 1d4+1} of the following features: small horns; fangs or sharp teeth; a forked tongue; catlike eyes; six fingers on each hand; goatlike legs; cloven hoofs; a forked tail; leathery or scaly skin; red or dark blue skin; cast no shadow or reflection; exude a smell of brimstone."
					],
					"type": "entries"
				},
				{
					"type": "entries",
					"name": "Winged",
					"entries": [
						"You have bat-like wings sprouting from your shoulder blades. You have a flying speed of 30 feet while you aren't wearing heavy armor."
					],
					"data": {
						"overwrite": "Infernal Legacy"
					}
				}
			],
			"overwrite": {
				"ability": true,
				"traitTags": true
			},
			"hasFluff": true,
			"hasFluffImages": true
		},
		{
			"name": "Zariel",
			"source": "MTF",
			"raceName": "Tiefling",
			"raceSource": "PHB",
			"page": 23,
			"ability": [
				{
					"cha": 2,
					"str": 1
				}
			],
			"additionalSpells": [
				{
					"innate": {
						"3": {
							"daily": {
								"1": [
									"searing smite#2"
								]
							}
						},
						"5": {
							"daily": {
								"1": [
									"branding smite"
								]
							}
						}
					},
					"ability": "cha",
					"known": {
						"1": [
							"thaumaturgy#c"
						]
					}
				}
			],
			"entries": [
				{
					"name": "Legacy of Avernus",
					"entries": [
						"You know the {@spell thaumaturgy} cantrip. When you reach 3rd level, you can cast the {@spell searing smite} spell as a 2nd-level spell once with this trait and regain the ability to do so when you finish a long rest. When you reach 5th level, you can cast the {@spell branding smite} spell once with this trait and regain the ability to do so when you finish a long rest. Charisma is your spellcasting ability for these spells."
					],
					"type": "entries",
					"data": {
						"overwrite": "Infernal Legacy"
					}
				}
			],
			"overwrite": {
				"ability": true
			},
			"hasFluff": true,
			"hasFluffImages": true
		},
		{
			"name": "Zariel",
			"source": "UAFiendishOptions",
			"raceName": "Tiefling",
			"raceSource": "PHB",
			"page": 2,
			"reprintedAs": [
				"Tiefling (Zariel)|MTF"
			],
			"ability": [
				{
					"cha": 2,
					"str": 1
				}
			],
			"additionalSpells": [
				{
					"innate": {
						"3": {
							"daily": {
								"1": [
									"searing smite#2"
								]
							}
						},
						"5": {
							"daily": {
								"1": [
									"branding smite"
								]
							}
						}
					},
					"ability": "cha",
					"known": {
						"1": [
							"thaumaturgy#c"
						]
					}
				}
			],
			"entries": [
				{
					"name": "Legacy of Avernus",
					"entries": [
						"You know the {@spell thaumaturgy} cantrip. When you reach 3rd level, you can cast the {@spell searing smite} spell as a 2nd-level spell once with this trait and regain the ability to do so when you finish a long rest. When you reach 5th level, you can cast the {@spell branding smite} spell once with this trait and regain the ability to do so when you finish a long rest. Charisma is your spellcasting ability for these spells."
					],
					"type": "entries",
					"data": {
						"overwrite": "Infernal Legacy"
					}
				}
			],
			"overwrite": {
				"ability": true
			}
		},
		{
			"name": "Envoy",
			"source": "UARacesOfEberron",
			"raceName": "Warforged",
			"raceSource": "UARacesOfEberron",
			"page": 69,
			"ability": [
				{
					"choose": {
						"from": [
							"str",
							"dex",
							"con",
							"int",
							"wis",
							"cha"
						],
						"count": 2
					}
				}
			],
			"traitTags": [
				"Tool Proficiency"
			],
			"skillProficiencies": [
				{
					"any": 1
				}
			],
			"entries": [
				{
					"type": "entries",
					"name": "Specialized Design",
					"entries": [
						"You gain one skill proficiency of your choice, one {@book tool|phb|5|tools} proficiency of your choice, and fluency in one language of your choice."
					]
				},
				{
					"type": "entries",
					"name": "Integrated Tool",
					"entries": [
						"Choose one tool you're proficient with. This tool is integrated into your body, and you double your proficiency bonus for any ability checks you make with it. You must have your hands free to use this integrated tool."
					]
				},
				{
					"type": "inset",
					"name": "Envoys: Specialized Design",
					"entries": [
						"As the name implies, most warforged were built to fight in the Last War. The vast majority of warforged are juggernauts or skirmishers\u2014soldiers and scouts who fought under the banner of one of the Five Nations. Warforged envoys, however, were designed to perform other functions. As an envoy, you have a skill, a tool proficiency, and a tool that's part of your body. When you make an envoy character, consider the following questions: What is your purpose? How does your skill and your tool reflect that purpose? What form does your integrated tool take? If you have embedded thieves' tools, for instance, are your fingers actually lockpicks, or can you produce keys from various parts of your body? The following characters are examples of warforged with integrated tools.",
						"{@b Lute} is a bard with the entertainer background; his namesake instrument folds out of his left arm.",
						"{@b Compass Rose} is a wizard with the outlander background. A keen explorer, she uses her built-in {@item cartographer's tools|phb} to record the paths she travels.",
						"{@b Masque} is an infiltrator. A rogue with the charlatan background and an integrated {@item disguise kit|phb}, she was built to blend in and assassinate. Cannith built six warforged of her design, and Masque has vowed to hunt down and destroy the other five.",
						"In developing your integrated tool, remember that you must have your hands free to use it. Masque, the infiltrator mentioned above, doesn't shapeshift like a changeling; she has to manually adjust her appearance."
					]
				}
			]
		},
		{
			"name": "Juggernaut",
			"source": "UARacesOfEberron",
			"raceName": "Warforged",
			"raceSource": "UARacesOfEberron",
			"page": 70,
			"ability": [
				{
					"str": 2
				}
			],
			"traitTags": [
				"Natural Weapon",
				"Powerful Build"
			],
			"entries": [
				{
					"type": "entries",
					"name": "Iron Fists",
					"entries": [
						"When you hit with an unarmed strike, you can deal {@dice 1d4} + your Strength modifier bludgeoning damage, instead of the normal damage for an unarmed strike."
					]
				},
				{
					"type": "entries",
					"name": "Powerful Build",
					"entries": [
						"You count as one size larger when determining your carrying capacity and the weight you can push, drag, or lift."
					]
				}
			]
		},
		{
			"name": "Skirmisher",
			"source": "UARacesOfEberron",
			"raceName": "Warforged",
			"raceSource": "UARacesOfEberron",
			"page": 70,
			"speed": 35,
			"ability": [
				{
					"dex": 2
				}
			],
			"entries": [
				{
					"type": "entries",
					"name": "Swift",
					"entries": [
						"Your walking speed increases by 5 feet."
					]
				},
				{
					"type": "entries",
					"name": "Light Step",
					"entries": [
						"When you are traveling alone for an extended period of time (one hour or more), you can move stealthily at a normal pace. (See {@book chapter 8|PHB|8|Travel Pace} of the Player's Handbook for information about travel pace.)"
					]
				}
			]
		}
	]
}
'''

json_data = json.loads(json_string)
json_data = limpar_entries(json_data["subrace"])
json_string_limpo = json.dumps(json_data)
print(json_string_limpo)