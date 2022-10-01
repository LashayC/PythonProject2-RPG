rooms = {

            'Upstairs Hall' : {
                'directions' : {
                    'north' : 'Attic',
                    'northeast' : 'Bathroom',
                    'east' : 'Office',
                    'west' : 'Your Bedroom',
                    'northwest' : 'Master Bedroom',
                    'south' : 'Stairs'
                    }
                },
            'Attic' : {
                'directions' : {
                    'north' : 'Upstairs Hall'
                    },
                'item' : ['rope'],
                'use' : ['lever'], #trapdoor to Downstairs Hall
                'need' : ['hangar']
                },
            'Your Bedroom' : {
                'directions' : {
                    'southeast' : 'Upstairs Hall'
                    },
                'item' : ['hangar'],
                },
            'Master Bedroom' : {
                'directions' : {
                    'east' : 'Upstairs Hall'
                    },
                'monster' : ['Skully the Skeleton'], #sleeping, take a bone
                'item' : ['bone']
                },
            'Bathroom' : {
                'directions' : {
                    'southwest' : 'Upstairs Hall'
                    },
                'monster' : ['Mary the Mirror Ghost'], #riddle adds door to south - through mirror to Otherside
                'need' : ['power', 'riddle answer']
                },
            'Office' : {
                'directions': {
                    'west' : 'Upstairs Hall'
                    },
                'monster' : ['Larry the Undead'], # gives hulu pwd
                'need' : ['full coffee mug'],
                },
            'Stairs' : {
                'directions' : {
                    'north' : 'Upstairs Hall',
                    'south' : 'Living Room'
                    }
                },
            'Entry Way' : {
                'directions': {
                    'west' : 'Living Room'
                    }
                },
            'Living Room' : {
                'directions' : {
                    'north' : 'Stairs',
                    'east' : 'Entry Way',
                    'west' : 'Downstairs Hall'
                    },
                'use' : ['tv'],
                'monster' : ['Paul the Poltergeist'], # after power appears
                'needs' : ['remote', 'power', 'hulu password', 'router'],
                },
            'Downstairs Hall' : {
                'directions' : {
                    'west' : 'Dining Room',
                    'east' : 'Kitchen',
                    'south' : 'Basement'
                    }
                },
            'Dining Room' : {
                'directions' : {
                    'east' : 'Downstairs Hall',
                    'south' : 'Kitchen',
                    'north' : 'Backyard'
                    },
                'item' : ['empty coffee mug']
                },
            'Kitchen' : {
                'directions' : {
                    'north' : 'Dining Room'
                    },
                'use' : ['coffee machine'],
                'need' : ['power', 'empty coffee mug']
                },
            'Backyard' : {
                'directions' : {
                    'south' : 'Dining Room'
                    },
                'monster' : ['Werewolf'],
                'item' : ['remote'],
                'need' : ['bone']
                },
            'Basement' : {
                'directions' : {
                    'north' : "Downstairs Hall"
                    },
                'use' : ['power switch'],
                'need' : ['rope']
                },
            'Otherside' : {
                'directions': {
                    'north' : 'Bathroom'
                    },
                'item' : ['router']
            }
        }
